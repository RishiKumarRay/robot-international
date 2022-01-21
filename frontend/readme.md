# Frontend

This directory contains the frontend codebase which is a [Flask](https://flask.palletsprojects.com). It's written in Python with [black](https://black.readthedocs.io/en/stable/) coding standards. Please refer to their docs for more info.

## Getting Started

To install the required dependencies:

```bash
pip install -r requirements.txt
```

To run the local development server:

```bash
python app.py
```

Open [http://localhost:5000](http://localhost:5000) with your browser to see the result.

Any edits to files in `app.py` will trigger hot-reloads. Edits to any HTML or Static content in either `static/` or `templates/` will not unfortunately.