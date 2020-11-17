#!/usr/bin/env bash

celery -A etl.celery_app worker -Q amazon_tasks_queue --pool=gevent --concurrency=50 --loglevel=info
