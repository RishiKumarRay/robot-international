# Leaderboards Website! 👀

[![build-frontend-linux](https://github.com/wholesome-series/wholesomemaker-web-flask/actions/workflows/build-frontend-linux.yml/badge.svg)](https://github.com/wholesome-series/wholesomemaker-web-flask/actions/workflows/build-frontend-linux.yml)

### Overview

Wholesomemaker using [Flask](https://flask.palletsprojects.com/) as Website Framework.

- [`app.py`](https://github.com/wholesome-series/wholesomemaker-web-flask/blob/master/app.py) Flask Framework in Python, obviously. 
- [`freezer.py`](https://github.com/wholesome-series/wholesomemaker-web-flask/blob/master/freeze.py) Static Website converter (Flask Freezer) 
- [`/templates`](https://github.com/wholesome-series/wholesomemaker-web-flask/tree/master/templates) Website templates in HTML (Flask formatted) 
- [`/static`](https://github.com/wholesome-series/wholesomemaker-web-flask/tree/master/static) web assets (css, js, and image)

### Frontend and Backend Development

To work on the frontend, you mostly only need to focus on the [`/templates`](https://github.com/wholesome-series/wholesomemaker-web-flask/tree/master/templates) directory. 

Run `python app.py` to start working on frontend development.

The frontend is deployed directly to [Github Pages](https://pages.github.com/) from the [`gh-pages`](https://github.com/wholesome-series/wholesomemaker-web-flask/tree/gh-pages) branch using this [Github Actions](https://github.com/wholesome-series/wholesomemaker-web-flask/actions/workflows/build-frontend-linux.yml).

On the other hand, Website backend are the [`app.py`](https://github.com/wholesome-series/wholesomemaker-web-flask/blob/master/app.py) itself.

Feel free to peek it out ✌