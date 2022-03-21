from pydoc import describe
from random import choices
from tokenize import String
from turtle import title
from wsgiref.validate import validator
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length


class PropForm(FlaskForm):
    title = StringField('Property Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    rooms = StringField('No. of Rooms', validators=[DataRequired()])
    bathrooms = StringField('No. of Bathrooms', validators=[DataRequired()])
    price = StringField('Price', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    propType = SelectField('Property Type', choices=[("House","House"),("Apartment","Apartment")])
    photo = FileField('Photos', validators=[FileRequired(), FileAllowed(["jpg","png"], "Images only!")])
