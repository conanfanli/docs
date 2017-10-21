VENV?=~/envs/rice

create-env:
	virtualenv -p python3.6 ${VENV}
	. ${VENV}/bin/activate && pip install -r requirements.txt


.PHONY: create-env
