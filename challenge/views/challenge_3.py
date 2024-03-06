from flask import render_template

from challenge import app


@app.route("/3/", methods=["GET", "POST"])
def  challenge_3() -> str:
    return render_template("challenge3.html")
