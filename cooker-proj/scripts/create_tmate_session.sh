#!/bin/bash
dime_bag_url=${dime_bag_url-`cat ~/.dime_bag_url`}


if [ -z "$dime_bag_url" ]; then
    echo missing dime_bag_url variable environment variable
    exit 1
fi

tmate -S /tmp/tmate.sock new-session -d
sleep 2

set -e

session=`tmate -S /tmp/tmate.sock display -p '#{tmate_web}'`

if [ -z "$session" ]; then
    echo cannot create tmate session
    exit 1
fi
echo session is $session
b64=`echo $session | base64`

url="${dime_bag_url}/$b64"
echo $url
curl "$url"
