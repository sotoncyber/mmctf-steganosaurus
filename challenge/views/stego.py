from urllib import request
from flask import render_template, views,jsonify
from flask import request as R
from challenge import app
from challenge.views import passcheck

@app.route('/checkpass', methods=['POST'])
def check_pass():
    input_text = R.json.get('input_text')
    result = passcheck.checkpass(input_text)
    return jsonify({'result': result})



class Challenge1View(views.View):
    template_name = "challenge1.html"

    def dispatch_request(self) -> str:
        return render_template(self.template_name)
app.add_url_rule("/1/", view_func=Challenge1View.as_view("challenge1"))

class Challenge2View(views.View):
    template_name = "challenge2.html"

    def dispatch_request(self) -> str:
        return render_template(self.template_name)
app.add_url_rule("/2/", view_func=Challenge2View.as_view("challenge2"))

class Challenge3View(views.View):
    template_name = "challenge3.html"

    def dispatch_request(self) -> str:
        return render_template(self.template_name)
app.add_url_rule("/3/", view_func=Challenge3View.as_view("challenge3"))

class Challenge4View(views.View):
    template_name = "challenge4.html"

    def dispatch_request(self) -> str:
        return render_template(self.template_name)
app.add_url_rule("/4/", view_func=Challenge4View.as_view("challenge4"))

class Challenge5View(views.View):
    template_name = "challenge5.html"

    def dispatch_request(self) -> str:
        return render_template(self.template_name)
app.add_url_rule("/5/", view_func=Challenge5View.as_view("challenge5"))

class Challenge6View(views.View):
    template_name = "challenge6.html"

    def dispatch_request(self) -> str:
        return render_template(self.template_name)
app.add_url_rule("/6/", view_func=Challenge6View.as_view("challenge6"))
