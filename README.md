# SRePs backend

Backend services for the SWE30010 project.

## Requirements

- Python 3.7.x
- PostgreSQL

## Installation

    git clone `repo url` && cd sreps\backend
    virtualenv ENV
    ENV/Scripts/activate
    pip install -r requirements.txt

Rename `.env.sample` to `.env` and provide the variables.

    python manage.py migrate
    python manage.py collectstatic
    python manage.py createsuperuser
    python manage.py runserver

## Deploying to Heroku

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=)

- Set the necessary environment variables.
- Run the above mentioned Django commands.
