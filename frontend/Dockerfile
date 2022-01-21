FROM python:3
COPY . /web
WORKDIR /web
RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir flask flask-pymongo pymongo dnspython python-dotenv gunicorn requests-oauthlib pyopenssl

EXPOSE 443

CMD [ "python", "app.py" ]