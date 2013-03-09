clean:
	@find . -name "*.pyc" -delete

deps:
	@pip install -r requirements.txt

setup: deps

run:
	@python manage.py runserver 0.0.0.0:8000

deploy:
	@git push git@heroku.com:pyne2013.git master

flake8:
	@flake8 . --exclude='.*migrations,.*manage.py' --ignore=E124,E128

help:
	grep '^[^#[:space:]].*:' Makefile | awk -F ":" '{print $$1}'
