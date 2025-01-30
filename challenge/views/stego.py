from flask import render_template, views

from challenge import app


class Challenge2View(views.View):
    template_name = "challenge2.html"

    def dispatch_request(self) -> str:
        return render_template(self.template_name)

class Challenge1View(views.View):
    template_name = "challenge1.html"

    def dispatch_request(self) -> str:
        return render_template(self.template_name)


app.add_url_rule("/2/", view_func=Challenge2View.as_view("challenge2"))
app.add_url_rule("/1/", view_func=Challenge1View.as_view("challenge1"))