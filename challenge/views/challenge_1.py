from flask import views

from challenge import app


class Challenge1View(views.MethodView):
    def get(self) -> str:
        return "Challenge 1 GET"

    def post(self) -> str:
        return "Challenge 1 POST"


app.add_url_rule("/1/", view_func=Challenge1View.as_view("challenge1"))
