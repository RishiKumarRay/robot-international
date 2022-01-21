FROM python:3

WORKDIR /usr/src/bot

RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir nextcord requests pymongo dnspython validators pygithub python-dotenv pillow millify nekos.py aiohttp algoliasearch

COPY . .

CMD [ "python", "main.py" ]