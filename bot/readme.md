### Development
We're using [black](https://black.readthedocs.io/en/stable/) coding standards. Please refer to their docs for more info.

### Testing/Workflow

To run the app, you need:

- A Discord server to test - you can't use the Wholesomeland/Warung International Discord Servers to do tests
- Python >= 3.9 - no guarantees on older versions
- A Discord bot with the 'Server Members Intent' and 'Presence Intent' enabled

If you don't own/admin a Discord server, creating one is simple, you can do it from the same menu you join discord
servers from.

#### Running with a database

If you want to develop features that require persisting data, spin up a MongoDB database. If you have Docker installed,
this is as simple as running `docker pull mongodb:latest` and `docker run mongodb` which will start a MongoDB container with a user `root` that has no
password. If you don't have Docker, you'll need to
[install MongoDB onto your system.](https://docs.mongodb.com/manual/installation/)

### Setup

```bash
# Make sure you're creating inside venv
python -m venv /path/to/your/venv

# then, Use the venv
./path/to/your/venv/scripts/activate.ps1

# Install the Dependencies first!
pip install -r requirements.txt

# Then, you can safely run the bot
python main.py
```