from flask import (
    Flask,
    render_template,
    g,
    session,
    redirect,
    request,
    url_for,
    jsonify,
)
from requests_oauthlib import OAuth2Session
from flask_pymongo import PyMongo
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

OAUTH2_CLIENT_ID = os.getenv("OAUTH2_CLIENT_ID")
OAUTH2_CLIENT_SECRET = os.getenv("OAUTH2_CLIENT_SECRET")
OAUTH2_REDIRECT_URI = os.getenv("REDIRECT_URI")
API_BASE_URL = os.environ.get("API_BASE_URL", "https://discord.com/api")
AUTHORIZATION_BASE_URL = API_BASE_URL + "/oauth2/authorize"
TOKEN_URL = API_BASE_URL + "/oauth2/token"
os.environ["AUTHLIB_INSECURE_TRANSPORT"] = "1"

app = Flask(__name__)
app.config["SECRET_KEY"] = OAUTH2_CLIENT_SECRET


def token_updater(token):
    session["oauth2_token"] = token


cluster = MongoClient(os.getenv("MONGODB_URI"))
levelling = cluster["dagelan"]["levelling"]
wm_levelling = cluster["discord"]["levelling"]


def make_session(token=None, state=None, scope=None):
    return OAuth2Session(
        client_id=OAUTH2_CLIENT_ID,
        token=token,
        state=state,
        scope=scope,
        redirect_uri=OAUTH2_REDIRECT_URI,
        auto_refresh_kwargs={
            "client_id": OAUTH2_CLIENT_ID,
            "client_secret": OAUTH2_CLIENT_SECRET,
        },
        auto_refresh_url=TOKEN_URL,
        token_updater=token_updater,
    )


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/login")
def login():
    scope = request.args.get("scope", "identify email guilds")
    discord = make_session(scope=scope.split(" "))
    authorization_url, state = discord.authorization_url(AUTHORIZATION_BASE_URL)
    session["oauth2_state"] = state
    return redirect(authorization_url)


@app.route("/leaderboard/922523614828433419")
def wi():
    rankings = levelling.find().sort("xp", -1)
    return render_template("wi_levels.html", rankings=list(rankings))


@app.route("/leaderboard/806949608349106197")
def wsv():
    rankings = wm_levelling.find().sort("xp", -1)
    return render_template("wsv_levels.html", rankings=list(rankings))


@app.route("/callback")
def callback():
    if request.values.get("error"):
        return request.values["error"]
    discord = make_session(state=session.get("oauth2_state"))
    token = discord.fetch_token(
        TOKEN_URL,
        client_secret=OAUTH2_CLIENT_SECRET,
        authorization_response=request.url,
    )
    session["oauth2_token"] = token
    return redirect(url_for(".me"))


@app.route("/me")
def me():
    discord = make_session(token=session.get("oauth2_token"))
    user = discord.get(API_BASE_URL + "/users/@me").json()
    guilds = discord.get(API_BASE_URL + "/users/@me/guilds").json()
    return jsonify(user=user, guilds=guilds)


@app.errorhandler(403)
def forbidden(error):
    return render_template("403.html")


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html")


@app.errorhandler(410)
def gone(error):
    return render_template("410.html")


@app.errorhandler(500)
def internal_server_error(error):
    return render_template("500.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=443, debug=True, ssl_context="adhoc")
