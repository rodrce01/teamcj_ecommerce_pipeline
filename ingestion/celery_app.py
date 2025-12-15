from celery import Celery
import os

import env_setup

celery_app = Celery(
	'amazon_tasks', #fetch products
	broker=os.environ["CELERY_BROKER_URL"], #figure out if we're using redis or rabbitMQ
	backend=os.environ["CELERY_RESULT_BACKEND"],
)
celery_app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="UTC",
)