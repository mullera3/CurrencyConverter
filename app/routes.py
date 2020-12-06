from flask import render_template ,url_for
from app import app
from app.forms import ConverterForm


@app.route('/')
@app.route('/index')
def index():
    form = ConverterForm()
    return render_template("index.html", title = "Home", form = form, )
