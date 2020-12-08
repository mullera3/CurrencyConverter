from flask_wtf import FlaskForm
from wtforms import SelectField, DecimalField
from wtforms.validators import DataRequired

class Country(FlaskForm):
    base_country = SelectField(label="Country",validators=[DataRequired()], choices=[])
    conversion_country = SelectField(label="Country", validators=[DataRequired()], choices=[])
    
    
