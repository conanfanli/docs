#!/bin/bash
docker exec -i tuktuk-web rm -rf /tmp/chunnel
docker cp ~/envs/tuktuk/lib/python3.6/site-packages/chunnel tuktuk-web:/tmp/chunnel

docker exec -i tuktuk-web chown root:root -R /tmp/chunnel

target=/usr/local/lib/python3.6/site-packages/chunnel
docker exec -i tuktuk-web rm -r $target

# docker exec -i tuktuk-web apk add rsync
docker exec -i tuktuk-web cp -rf /tmp/chunnel $target
