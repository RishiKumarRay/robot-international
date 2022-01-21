FROM python:3

WORKDIR /bot

RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . /usr/src/bot

CMD [ "python", "main.py" ]