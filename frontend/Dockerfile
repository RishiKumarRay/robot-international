FROM python:3

WORKDIR /usr/src/frontend

RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir flask flask-pymongo pymongo dnspython python-dotenv gunicorn requests-oauthlib pyopenssl

COPY . /usr/src/frontend

EXPOSE 443

CMD [ "python", "app.py" ]