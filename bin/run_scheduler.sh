#!/usr/bin/env bash

rm celerybeat.pid

# Run celery beat for scheduling background tasks
celery -A etl.celery_app beat --loglevel=info
