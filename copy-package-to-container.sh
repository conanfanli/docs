#!/bin/bash

RED='\033[0;31m'
NO_COLOR='\033[0m' # No Color

container_name=$1
package_name=$2

ECHO() {
    echo -e "[+] ${RED}$@${NO_COLOR}"
}

show-usage() {
    echo ./copy.sh container_name package_name
    exit 1
}
if [ -z $VIRTUAL_ENV ]
then
    echo Must be in virtual environment or define VIRUTAL_ENV env var
    exit 1
fi

if [ -z "$package_name" ] || [ -z "$container_name" ]
then
    show-usage
fi


run-docker-command() {
    # echo command to run: $@ on $container_name
    docker exec -it $container_name $@
}


TMP=/tmp/$package_name
SOURCE_DIR=$VIRTUAL_ENV/lib/python3.6/site-packages/$package_name
TARGET=/usr/local/lib/python3.6/site-packages/$package_name


ECHO removing $TMP
run-docker-command "rm -rf $TMP"

ECHO copying $SOURCE_DIR to $container_name:$TMP
docker cp -aL $SOURCE_DIR $container_name:$TMP

ECHO changing owner
run-docker-command "chown root:root -R $TMP"

ECHO removing $TARGET
run-docker-command "rm -r $TARGET"

ECHO copying files to $TARGET
run-docker-command "cp -rf $TMP $TARGET"

ECHO listing copied files
run-docker-command "ls -al $TARGET"

