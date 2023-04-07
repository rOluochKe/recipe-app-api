# Recipe app API

A complete app API

## Technologies

- Python
- Django
- Django Rest Framework
- PostgreSQL
- Docker
- Unittest

## Setup

### Dev Environment

- Build `docker-compose build`
- Run app `docker-compose up`
- Docker down `docker-compose down`
- Lint `docker-compose run --rm app sh -c "python manage.py wait_for_db && flake8"`
- Tests `docker-compose run --rm app sh -c "python manage.py wait_for_db && python manage.py test"`
- Make migrations `docker-compose run --rm app sh -c "python manage.py wait_for_db && python manage.py makemigrations"`
- Run migrate `docker-compose run --rm app sh -c "python manage.py wait_for_db && python manage.py migrate"`
- Create super user `docker-compose run --rm app sh -c "python manage.py wait_for_db && python manage.py createsuperuser"`

### Deploy

- Down `docker-compose -f docker-compose-deploy.yml down`
- Run `docker-compose -f docker-compose-deploy.yml up`
