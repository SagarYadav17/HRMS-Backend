# Human Resource Management System

Backend Service for a Human Resource Management System.

## Tech Stack

**Framework:** [Django](https://www.djangoproject.com/) with [Rest Framework](https://www.django-rest-framework.org/)

**Database:** PostgreSQL

## Installation and Usage

- Create conda environment and install python

  ```bash
  conda create -n hrms
  conda activate hrms
  conda install python=3.10.4
  ```

- Install dependencies

  ```bash
  pip install -r requirements.txt --no-cache
  ```

- Host Postgres Database using Docker

  ```bash
  docker run -p 5432:5432 --name hrms -e POSTGRES_DB=hrms -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=postgres -d postgres
  ```

  - Database Name: hrms
  - User: postgres
  - Password: postgres
  - Host: 127.0.0.1 (localhost)
  - Port: 5432

- Migrate and Run the server
  ```bash
  python manage.py migrate
  python manage.py runserver
  ```
