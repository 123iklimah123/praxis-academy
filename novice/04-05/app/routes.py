from app.controllers import buah
from app import app

app.route("/", methods=["GET", "POST"])(buah.index)