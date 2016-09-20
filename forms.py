"""Module for all WTF form definitions"""
from flask_wtf import Form
from wtforms.fields import TextField,DateField,StringField,SubmitField, SelectField
from wtforms.validators import DataRequired, Regexp, ValidationError, URL
import requests

# http://wtforms.readthedocs.io/en/latest/fields.html#basic-fields

__author__ = 'eljefeloco'


def url_exists(form,field):
    page=requests.head(field.data)
    if not page.status_code in (200,301):
        raise ValidationError("The review url doesn't point to a valid page")


class ReviewForm(Form):
    formwho = StringField(
        "Author",
        default="Lee",
        validators=[DataRequired("You must enter an author"),
                    Regexp(r"^[A-Za-z0-9_]+$",message="Author should be letters and numbers only")
                    ])
    formtagline = StringField(
        "Tagline",
        default="Lee",
        validators=[DataRequired("You must enter a tagline")
                    ])
    formurl = StringField(
        "Review URL",
        default="https://www.google.com",
        validators=[DataRequired("You must enter a url"),
                    url_exists]
    )
    formwhen = StringField("Review Date (Jan-2016,Mar-2015)",
                           default="Jan-2016",
                           validators=[DataRequired("Need to enter a date")])
    formreviewof = StringField("Review Of",
                               validators=[Regexp("^[\w ]*",message="Words only please")])
    formtheme = SelectField("Theme",
                            choices=[('wrapper.html','Wrapper'),('straight.html','Straight')],
                            validators=[DataRequired("Pleas enter a theme")])
    rewiewsep = StringField("Review Separator",default=" * ")
    rewiewheading = StringField("Heading",default="Recent Reviews")
    headchar = StringField("Underline Chracter for Heading",default="-")
    formsubmit = SubmitField("Generate")


class URLForm(Form):
    ReviewURL = StringField(
        "Review URL",
        default="http://independentgirls.com/indiboard/index.php/topic/502060-1pretty-lady/",
        validators=[
            DataRequired("You must enter the review URL"),
            URL("Invalid URL Format"),
            url_exists])
    formsubmit = SubmitField("Generate")