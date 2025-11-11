from celery import Celery

app = Celery(
	'fetch_products',
	broker='', #figure out if we're using redis or rabbitMQ
	backend=''
)

import ingestion.tasks