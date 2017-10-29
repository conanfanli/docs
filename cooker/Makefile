.PHONY: restore-db
restore-db:
	psql -U postgres cooker -c 'drop schema public cascade; create schema public'
	python manage.py migrate

.PHONY: test
test:
	pip install -r requirements.txt
	python manage.py test

.PHONY: load-current
load-current:
	python manage.py loaddata current

.PHONY: dropschema
dropschema:
	psql cooker -c 'drop schema public cascade; create schema public'

.PHONY: dump-current
dump-current:
	python manage.py dumpdata --indent=2 core -o cooker/core/fixtures/current.json

.PHONY: dump-live-data
dump-live-data:
	DATABASE_URL=$(shell heroku config:get DATABASE_URL) python manage.py dumpdata --indent=2 core -o cooker/core/fixtures/current.json


.PHONY: start-dev
start-dev:
	honcho start -f Procfile.dev

.PHONY: deploy-static
deploy-static:
	git branch | grep '* master'
	git st | grep -o 'working directory clean'
	git co static-deploy && git pull && git merge master
	python manage.py collectstatic --no-input
	npm run build
	cp -r dist/* staticfiles/
	rm -r public
	mv staticfiles public
	git add public
	git commit -m 'new deploy'
	git push
	git co master

.PHONY: prod-start
prod-start:
	heroku ps:scale web=1

.PHONY: prod-stop
prod-stop:
	heroku ps:scale web=0
