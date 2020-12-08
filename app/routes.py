from flask import render_template ,url_for
from app import app
from app.forms import ConverterForm
from app.country import Country


@app.route('/')
@app.route('/index')
def index():
    form = ConverterForm()
    country = Country()
    return render_template("index.html", title = "Home", form = form, country = country)
