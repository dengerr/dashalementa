runserver:
	~/soft/google-cloud-sdk/bin/dev_appserver.py app.yaml

deploy:
	~/soft/google-cloud-sdk/bin/gcloud app deploy
	~/soft/google-cloud-sdk/bin/gcloud app browse
