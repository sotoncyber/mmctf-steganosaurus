from flask import render_template

from challenge import app

from . import (
    stego,  # noqa: F401
)


@app.route("/", methods=["GET"])
def index() -> str:
    return render_template("index.html")
