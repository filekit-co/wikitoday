import asyncio
import base64
import json
import logging
from typing import List

import httpx

from app.config import get_env
from domain.entities import Folder
from src.consts import TargetCountryCode

logger = logging.getLogger(__name__)
_env = get_env()

# git file mode, the number 100644 means that this is a regular file
GIT_REGULAR_FILE_TYPE = "100644"

# 설정값
owner = _env["GITHUB_OWNER"]
repo = _env["GITHUB_REPOSITORY"]
base_path = _env["GITHUB_BASE_PATH"]
token = _env["GITHUB_TOKEN"]
branch = _env["GITHUB_BRANCH"]

blob_url = f"https://api.github.com/repos/{owner}/{repo}/git/blobs"
tree_url = f"https://api.github.com/repos/{owner}/{repo}/git/trees"
commit_url = f"https://api.github.com/repos/{owner}/{repo}/git/commits"
sha_url = f"https://api.github.com/repos/{owner}/{repo}/git/refs/heads/{branch}"

# 요청 헤더를 구성합니다
headers = {
    "Accept": "application/vnd.github+json",
    "Authorization": f"Bearer {token}"
}

async def create_blob(client: httpx.AsyncClient, content: str, path: str) -> tuple[str, str]:
    payload = {
        "content": base64.b64encode(content.encode()).decode(),
        "encoding": "base64"
    }
    try:
        response = await client.post(blob_url, headers=headers, data=json.dumps(payload))
        response.raise_for_status()
        return (response.json()["sha"], path)
    except httpx.HTTPStatusError as e:
        logging.error(f"An error occurred while creating blob: {e}")
        logging.error(f"Error message: {e.response.text}")

async def create_tree(client: httpx.AsyncClient, base_tree: str, blobs: List[dict]):
    payload = {
        "base_tree": base_tree,
        "tree": blobs
    }
    try:
        response = await client.post(tree_url, headers=headers, data=json.dumps(payload))
        response.raise_for_status()
        return response.json()["sha"]
    except httpx.HTTPStatusError as e:
        logging.error(f"An error occurred while creating tree: {e}")
        logging.error(f"Error message: {e.response.text}")

async def create_commit(client: httpx.AsyncClient, tree: str, parents: List[str], message: str):
    payload = {
        "tree": tree,
        "parents": parents,
        "message": message
    }
    try:
        response = await client.post(commit_url, headers=headers, data=json.dumps(payload))
        response.raise_for_status()
        return response.json()["sha"]
    except httpx.HTTPStatusError as e:
        logging.error(f"An error occurred while creating commit: {e}")
        logging.error(f"Error message: {e.response.text}")

async def update_commit_sha(client: httpx.AsyncClient, commit: str):
    payload = {
        "sha": commit
    }
    try:
        response = await client.patch(sha_url, headers=headers, data=json.dumps(payload))
        response.raise_for_status()
    except httpx.HTTPStatusError as e:
        logging.error(f"An error occurred while updating SHA: {e}")
        logging.error(f"Error message: {e.response.text}")

# 1. get commit sha
async def get_commit_sha(client: httpx.AsyncClient) -> str:
    try:
        response = await client.get(sha_url, headers=headers)
        response.raise_for_status()
        current_commit = response.json()["object"]["sha"]
        return current_commit
    except httpx.HTTPStatusError as e:
        logging.error(f"An error occurred while getting commit SHA: {e}")
        logging.error(f"Error message: {e.response.text}")

async def get_tree_sha(client: httpx.AsyncClient, commit_sha: str) -> str:
    try:
        response = await client.get(f"{commit_url}/{commit_sha}", headers=headers)
        response.raise_for_status()
        tree_sha = response.json()["tree"]["sha"]
        return tree_sha
    except httpx.HTTPStatusError as e:
        logging.error(f"An error occurred while getting tree SHA: {e}")
        logging.error(f"Error message: {e.response.text}")

async def push_folders(folders: List[Folder], country: TargetCountryCode):
    today = folders[0].today
    commit_msg = f"docs: {country} {today} articles"
    
    async with httpx.AsyncClient() as client:
        # 1. Get the current commit object
        commit_sha = await get_commit_sha(client)
        # 2. Retrieve the tree it points to
        tree_sha = await get_tree_sha(client, commit_sha)
        
        # 3. Create blobs and build up tree
        new_tree = []
        tasks = []
        for folder in folders:
            for markdown in folder.mds:
                path = f'{base_path}/{folder.today}/{folder.folder_name}/{markdown.language}.md'
                tasks.append(create_blob(client, markdown.md, path))
        blob_shas = await asyncio.gather(*tasks)

        for sha, path in blob_shas:
            new_tree.append({
                "path": path,
                "mode": GIT_REGULAR_FILE_TYPE,  # This is the file_mode
                "type": "blob",
                "sha": sha
            })

        # 4. Create a new tree with the new files
        new_tree_sha = await create_tree(client, tree_sha, new_tree)

        # 5. Create a new commit pointing to the new tree
        new_commit_sha = await create_commit(
            client, new_tree_sha, 
            [commit_sha], 
            message = commit_msg
        )

        # 6. Update the reference
        await update_commit_sha(client, new_commit_sha)