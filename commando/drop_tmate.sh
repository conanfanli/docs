#!/bin/bash
machine_name=${machine_name-$1}
secret=${secret}


if [ -z "$machine_name" ]; then
    echo Missing machine name!!!
    exit 1
fi

if [ -z "$secret" ]; then
    echo missing secret variable environment variable
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
url="https://dropping-dimes.herokuapp.com/${secret}=/set/tmate-$machine_name/$b64"
echo $url
curl "$url"
