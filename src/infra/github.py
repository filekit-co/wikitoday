import asyncio
import base64
import json
import logging

import httpx

from app.config import get_env
from domain.entities import Folder, Markdown

_env = get_env()


# 설정값
owner = _env["GITHUB_OWNER"]
repo = _env["GITHUB_REPOSITORY"]
path = _env["GITHUB_BASE_PATH"]
token = _env["GITHUB_TOKEN"]

# BASE URL을 구성합니다
# base_url = f"https://api.github.com/repos/{owner}/{repo}/contents/{path}"
base_url = f"https://api.github.com/repos/{repo}/contents/{path}"

# 요청 헤더를 구성합니다
headers = {
    "Accept": "application/vnd.github+json",
    "Authorization": f"Bearer {token}"
}

# https://docs.github.com/ko/rest/repos/contents?apiVersion=2022-11-28#create-or-update-file-contents
async def push_markdown(client: httpx.AsyncClient, folder: Folder, markdown: Markdown):
    markdown_dir = f'{folder.today}/{folder.folder_name}/{markdown.language}.md'
    url = f'{base_url}/{markdown_dir}'

    # 저장하려는 텍스트 데이터 (Markdown)
    data = markdown.md
    # 문자열을 base64로 인코딩합니다.
    content = base64.b64encode(data.encode()).decode()

    commit_message = f"docs: Update {markdown_dir}"
    payload = {
        "message": commit_message,
        "content": content,
    }
    
    # 파일 생성 또는 업데이트 요청을 보냅니다.
    try:
        response = await client.put(url, headers=headers, data=json.dumps(payload))
        response.raise_for_status()
    except httpx.HTTPStatusError as e:
        logging.error(f"An error occurred: {e}")
        logging.error(f"Error message: {e.response.text}")


async def push_folder(folder):
    # 비동기 클라이언트 생성
    async with httpx.AsyncClient() as client:
        tasks = [push_markdown(client, folder, markdown) for markdown in folder.mds]
        # 폴더의 각 Markdown에 대해 push_markdown 호출
        await asyncio.gather(*tasks)
