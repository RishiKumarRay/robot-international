FROM python:3
COPY . /app
WORKDIR /app
RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir nextcord requests pymongo dnspython validators pygithub python-dotenv pillow millify nekos.py aiohttp algoliasearch
CMD [ "python", "main.py" ]