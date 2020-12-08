from flask_wtf import FlaskForm
from wtforms import DecimalField, BooleanField, SubmitField, SelectField, StringField
from wtforms.validators import DataRequired
from datetime import date
import pandas as pd


class ConverterForm(FlaskForm):
    date = date.today().strftime("%d/%m/%Y")
    amount = DecimalField(label=" Amount ", validators=[DataRequired()])

country_list_df = pd.read_json(
    "/Users/amanimuller/Desktop/Projects/CurrencyConverter/app/data/data_json.json")
country_abbreviations = country_list_df["Code"]

class Country(FlaskForm):
    base_country = SelectField(label="Country", validators=[DataRequired()], choices=country_abbreviations)
    conversion_country = SelectField(label="Country", validators=[DataRequired()], choices=country_abbreviations)
    