IAM = sa-minwook@poetic-producer-396107.iam.gserviceaccount.com

# Google Cloud 명령어
GC_PREFIX = gc

$(GWF_PREFIX)-auth:
	gcloud auth login

$(GWF_PREFIX)-info:
	gcloud info --show-log

# Google Cloud Workflow 명령어
GWF_PREFIX = gwf
GWF_NAME = myFirstWorkflow


$(GWF_PREFIX)-deploy:
	@gcloud workflows deploy $(GWF_NAME) --source=./workflows/$(GWF_NAME).yaml --service-account=$(IAM)

$(GWF_PREFIX)-run:
	@gcloud workflows run $(GWF_NAME) --data='{"searchTerm": "north"}'

$(GWF_PREFIX)-desc:
	@gcloud workflows describe $(GWF_NAME)

$(GWF_PREFIX)-list:
	@gcloud workflows list

$(GWF_PREFIX)-del:
	@gcloud workflows delete $(GWF_NAME)


# Google Cloud Run 명령어
GCR_PREFIX = gcr
GCR_NAME = ...
GCR_IMG_NAME = ...

$(GCR_PREFIX)-deploy:
	@gcloud run deploy $(GCR_NAME) --image=$(GCR_IMG_NAME)

$(GCR_PREFIX)-describe:
	@gcloud run services describe $(GCR_NAME)

$(GCR_PREFIX)-list:
	@gcloud run services list

.PHONY: $(GC_PREFIX)-auth $(GC_PREFIX)-info $(GWF_PREFIX)-deploy $(GWF_PREFIX)-run $(GWF_PREFIX)-desc $(GWF_PREFIX)-list $(GWF_PREFIX)-del $(GCR_PREFIX)-deploy $(GCR_PREFIX)-describe $(GCR_PREFIX)-list
