PROJECT_ID = poetic-producer-396107
IAM = sa-minwook@poetic-producer-396107.iam.gserviceaccount.com
PROJECT_NUMBER := $(shell gcloud projects describe $(PROJECT_ID) --format='value(projectNumber)')
CLOUDBUILD_SA := $(PROJECT_NUMBER)@cloudbuild.gserviceaccount.com

PROTOBUF_DIR = /Users/minwook/code/filekit/wikitoday/v2/libs/protobuf

compile-proto:
	@protoc -I=$(PROTOBUF_DIR) --python_out=$(PROTOBUF_DIR) $(PROTOBUF_DIR)/*.proto

enable:
	@gcloud services enable \
    run.googleapis.com \
    cloudbuild.googleapis.com

perm:
	@gcloud projects add-iam-policy-binding $(PROJECT_ID) \
    --member=serviceAccount:${IAM} \
    --role=roles/run.admin
	@gcloud projects add-iam-policy-binding $(PROJECT_ID) \
    --member=serviceAccount:${IAM} \
    --role=roles/cloudbuild.builds.editor

build-perm:
	@gcloud projects add-iam-policy-binding $(PROJECT_ID) \
    --member=serviceAccount:${CLOUDBUILD_SA} \
    --role=roles/run.admin
	@gcloud projects add-iam-policy-binding $(PROJECT_ID) \
    --member=serviceAccount:${CLOUDBUILD_SA} \
    --role=roles/cloudbuild.builds.editor
	@gcloud projects add-iam-policy-binding $(PROJECT_ID) \
    --member=serviceAccount:${CLOUDBUILD_SA} \
    --role=roles/iam.serviceAccountUser