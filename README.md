# Recipe app API

This full API service for your favorite recipes application is built using Python, Django, Django Rest Framework (DRF), PostgreSQL, and Docker, providing a comprehensive solution for managing and sharing your favorite recipes.

Python serves as the core programming language, while Django offers a robust framework for developing web applications. DRF extends Django's capabilities, enabling the creation of powerful and flexible APIs for recipe management.

The PostgreSQL database ensures reliable and scalable data storage, allowing users to store and retrieve their favorite recipes efficiently.

By utilizing Docker, the application guarantees easy deployment and scalability, enabling seamless integration with existing infrastructure.

Through this API service, users can perform various recipe-related operations, such as creating, updating, and deleting recipes, as well as searching and filtering recipes based on different criteria.

The combination of Python, Django, DRF, PostgreSQL, and Docker empowers users to create a customized and user-friendly recipe application, enabling them to share and explore their favorite recipes with ease.


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

### Updating app

- Volume down `docker-compose down --volumes`
