from flask_wtf import FlaskForm
from wtforms import DecimalField, BooleanField, SubmitField, SelectField, StringField
from wtforms.validators import DataRequired
from datetime import date
import pandas as pd
import calendar

country_list_df = pd.read_json(
    "/Users/amanimuller/Desktop/Projects/CurrencyConverter/app/data/data_json.json")
country_abbreviations = country_list_df["Code"]

month = date.today().strftime('%m')
day = date.today().strftime('%d')
year = date.today().strftime('%Y')

class ConverterForm(FlaskForm):
    date = str(calendar.month_abbr[int(month)]) + '/' + day + '/' + year
    amount = DecimalField(label=" Amount ", validators=[DataRequired()])


class Country(FlaskForm):
    base_country = SelectField(label="Country", validators=[DataRequired()], choices=country_abbreviations)
    conversion_country = SelectField(label="Country", validators=[DataRequired()], choices=country_abbreviations)
    
