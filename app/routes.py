from app import app
from app.forms import SearchFrom


from flask import render_template


@app.route("/")
@app.route("/index")
def index():
    form = SearchFrom()
    return render_template("index.html", form = form)

