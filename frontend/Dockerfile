FROM python:3

WORKDIR /frontend

# We copy just the requirements.txt first to leverage Docker cache
COPY requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY . /app

EXPOSE 443

CMD [ "python", "app.py" ]