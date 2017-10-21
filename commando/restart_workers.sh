#!/bin/bash

docker exec -i tuktuk-worker sh -c 'ps aux | grep "celery worker" | grep -v grep | awk "{print \$1}"| xargs kill -HUP'
