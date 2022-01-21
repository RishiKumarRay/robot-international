FROM python:3

RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir nextcord requests pymongo dnspython validators pygithub python-dotenv pillow millify nekos.py aiohttp algoliasearch

COPY . /usr/src/bot
WORKDIR /usr/src/bot

CMD [ "python", "main.py" ]