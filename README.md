# SUCSS Challenge Template
[![Python static type/format checks](https://github.com/sotoncyber/challenge_template/actions/workflows/checks.yaml/badge.svg)](https://github.com/sotoncyber/challenge_template/actions/workflows/checks.yaml)

This template repository contains all the required files to start a simple challenge.

## Setup

Ensure you have python poetry installed - this is used to install a virtualenv and manage dependencies

```
pip install --upgrade pip --user
pip3 install poetry
python -m poetry install --no-root
```

## Running in development

Flask comes with a development server built in. To use it, run
```
python -m poetry run flask -A challenge run
```

## Running in production

```
python -m poetry run gunicorn 'challenge:app'
```

## Running with docker

```
docker-compose -p "<project name>" -f "docker/compose.yaml" up --build
```