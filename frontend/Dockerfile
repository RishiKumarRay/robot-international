FROM python:3

WORKDIR /frontend

RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . /usr/src/frontend

EXPOSE 443

CMD [ "python", "app.py" ]