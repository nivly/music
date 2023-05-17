# This file is where data entry forms are created. Forms are placed on templates 
# and users fill them out.  Each form is an instance of a class. Forms are managed by the 
# Flask-WTForms library.

from flask_wtf import FlaskForm
import mongoengine.errors
from wtforms.validators import URL, Email, DataRequired
from wtforms.fields.html5 import URLField
from wtforms import StringField, SubmitField, TextAreaField, IntegerField, SelectField, FileField, BooleanField

class ProfileForm(FlaskForm):
    fname = StringField('First Name', validators=[DataRequired()])
    lname = StringField('Last Name', validators=[DataRequired()]) 
    image = FileField("Image") 
    submit = SubmitField('Post')
    role = SelectField('Role',choices=[("ADMIN","ADMIN"),("CUSTOMER","CUSTOMER")])

class BlogForm(FlaskForm):
    subject = StringField('title of merch', validators=[DataRequired()])
    content = TextAreaField('price', validators=[DataRequired()])
    tag = StringField('size', validators=[DataRequired()])
    image = FileField("Image")
    submit = SubmitField('post')

class ProjectsForm(FlaskForm):
    subject = StringField('title of merch', validators=[DataRequired()])
    content = TextAreaField('price', validators=[DataRequired()])
    tag = StringField('size', validators=[DataRequired()])
    image = FileField("Image")
    submit = SubmitField('post')


class CommentForm(FlaskForm):
    content = TextAreaField('Comment', validators=[DataRequired()])
    submit = SubmitField('Comment')

class ClinicForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    streetAddress = StringField('Address', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    state = StringField('State', validators=[DataRequired()])
    zipcode = StringField('Zipcode',validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    submit = SubmitField('Submit')
