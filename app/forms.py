from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, EmailField
from wtforms.validators import DataRequired, EqualTo, Email


class SearchFrom(FlaskForm):
    query = StringField("Search", validators=[DataRequired()], render_kw={"placeholder": "Search any subject"})