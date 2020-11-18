#!/usr/bin/env bash

# directories for logs
mkdir -p /tony/data/logs/web/

# run web server

gunicorn --reload --access-logfile "-" --error-logfile "-" --log-level debug --worker-class gevent --workers=3 --timeout 60 --bind 0.0.0.0:8081 web.manage:app
