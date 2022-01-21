# Warung International & Wholesomeland Web Services

[![build-frontend-linux](https://github.com/wholesomeland/web/actions/workflows/build-frontend-linux.yml/badge.svg)](https://github.com/wholesomeland/web/actions/workflows/build-frontend-linux.yml) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

This monorepo contains the web services for Warung International & Wholesomeland Discord Servers.

We're using [Flask](https://flask.palletsprojects.com/) as our Website Framework. 

## Overview

- [`app.py`](app.py) Flask Framework in Python, obviously. 
- [`test.py`](test.py) For testing MongoDB Connections through our website
- [`wsgi.py`](test.py) WSGI systems for production uses 
- [`/templates`](/templates) Website templates in HTML (Flask formatted) 
- [`/static`](/static) our web assets (css, js, and image)

## Frontend and Backend Development

To work on the frontend, you mostly only need to focus on the [`/templates`](/templates) directory. 

Run `python app.py` to start working on frontend development.

## Deployment

The frontend is deployed directly to [Heroku](https://heroku.com/) from the `master` branch using this [Github Actions](/.github/workflows/build-frontend-linux.yml).