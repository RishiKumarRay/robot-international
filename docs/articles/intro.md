# Getting Started

All you need to know to "How to setup a environment for Testing/Contributing/Use this source code".

## Testing/Workflow

To run the app, you need:

- A Discord Bot, with `server member intent` and `presence intent`.. obviously.. [click here](https://discord.com/developers/applications)
- A Discord server to test - you can't use the Wholesome Series Videos Discord Server to do tests
- [Python version 3.10.0](https://www.python.org/downloads/release/python-3100/) - no guarantees on older versions
- A MongoDB Server for levelling and warning system (Pick one)
  - [MongoDB Community Server (Offline)](https://www.mongodb.com/try/download/community)
  - [MongoDB Atlas (Online)](https://www.mongodb.com/cloud/atlas)
- A Good Code IDE, obviously.. I recommend you [Visual Studio Code](https://code.visualstudio.com)

If you don't own/admin a Discord server, creating one is simple, you can do it from the same menu you join discord servers from.

## .env systems

We're starting to implement the `.env` files.

<del>We don't provide the examples, _yet._</del> 

There's an example `./.env` on root folder, but.. it's optimized for Production use cases scenario. 
Feel free to use it as your starting guide! :v:

Feel free to use these as your starting guide! :v:

```bash
VERSION="refer to main.py file"
BOT_TOKEN="https://discord.com/developers/applications"
MONGODB_URL="your mongodb uri's"
GITHUB_TOKEN="your github token"
GIST_ID="provide your github gist id for readme commands!"
GIST_ID2="provide your github gist id for role info commands!"
RAPID_API_KEY="for urban and dadjokes commands"
MAIN_INVITE="provide your server invite"
STICKER_INVITE="provide your sticker server invite (optional)"
```

## Docker

Thanks to [🐧 rsetiawan7](https://github.com/rsetiawan7), Wholesomemaker Supports running on Docker. but.. the Active Docker Images has been used for Production Purposes as a Private Repository.

You "could" technically run it on Docker, I have provide you the essence of it (Dockerfile and github actions settings).

I assume you already know how to do it, Please Refer to [`Docker`](https://github.com/Matthew-Soft/Wholesomemaker/tree/master/Docker) folder to Getting Started. Thanks. 😉