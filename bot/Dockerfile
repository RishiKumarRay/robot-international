FROM python:3

WORKDIR /bot

RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir nextcord requests pymongo dnspython validators pygithub python-dotenv pillow millify nekos.py aiohttp algoliasearch

COPY . /usr/src/bot

CMD [ "python", "/usr/src/bot/main.py" ]