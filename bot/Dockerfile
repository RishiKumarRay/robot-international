FROM python:3

WORKDIR /usr/src/bot

COPY ./bot/requirements.txt ./
RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "main.py" ]