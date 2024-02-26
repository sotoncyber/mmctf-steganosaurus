from flask import render_template

from challenge import app

from . import (
    challenge_1,  # noqa: F401
    challenge_2,  # noqa: F401
)


@app.route("/", methods=["GET"])
def index() -> str:
    return render_template("index.html")
