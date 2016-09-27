"""Module for all WTF form definitions"""
from flask_wtf import Form
from wtforms.fields import TextField, StringField, SubmitField, SelectField, BooleanField
from wtforms.validators import DataRequired, Regexp, ValidationError, URL
import requests
from models import Review

# http://wtforms.readthedocs.io/en/latest/fields.html#basic-fields

__author__ = 'eljefeloco'


def url_exists(form, field):
    page = requests.head(field.data)
    if page.status_code not in (200, 301):
        raise ValidationError("The review url doesn't point to a valid page")

    try:
        Review.from_page(field.data)
    except:
        raise ValidationError("Are you sure that's a review?")


class ReviewForm(Form):
    formwho = StringField(
        "Author",
        default="Lee",
        validators=[DataRequired("You must enter an author"),
                    Regexp(r"^[A-Za-z0-9_]+$", message="Author should be letters and numbers only")
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
                               validators=[Regexp("^[\w ]*", message="Words only please")])
    formtheme = SelectField("Theme",
                            choices=[
                                ('wrapped.html', 'Wrapper'),
                                ('inline.html', 'Straight'),
                                ('centered_column.html','Centered Column')],
                            validators=[DataRequired("Please enter a theme")])
    rewiewsep = StringField("Review Separator", default=" * ")
    rewiewheading = StringField("Heading", default="Recent Reviews")
    headchar = StringField("Underline Chracter for Heading", default="-")
    formsubmit = SubmitField("Generate")


class URLForm(Form):
    ReviewURL = StringField(
        "Review URL",
        #default="http://independentgirls.com/indiboard/index.php/topic/502060-1pretty-lady/",
        validators=[
            DataRequired("You must enter the review URL"),
            URL("Invalid URL Format"),
            url_exists])
    formsubmit = SubmitField("Add Review")
    formtheme = SelectField("Theme",
                            choices=[
                                ('wrapped.html', 'Wrapper'),
                                ('inline.html', 'Straight'),
                                ('centered_column.html','Centered Column')],
                            validators=[DataRequired("Pleas enter a theme")])
    rewiewsep = StringField("Review Separator", default=" * ")
    rewiewheading = StringField("Heading", default="Recent Reviews")
    headchar = StringField("Underline Character for Heading", default="-")
    formheadfont = SelectField("Heading Font", choices=[
        ('arial,helvetica,sans-serif', 'arial'),
        ('comic sans ms,cursive', 'comic sans ms'),
        ('courier new,courier,monospace', 'courier new'),
        ('georgia,serif', 'georgia'),
        ('lucida sans unicode,lucida grande,sans-serif',
         'lucida sans unicode'),
        ('tahoma,geneva,sans-serif', 'tahoma'),
        ('times new roman,times,serif', 'times new roman'),
        ('trebuchet ms,helvetica,sans-serif', 'trebuchet ms'),
        ('verdana,geneva,sans-serif', 'verdana')])
    formbodyfont = SelectField("Body Font", choices=[
        ('arial,helvetica,sans-serif', 'arial'),
        ('comic sans ms,cursive', 'comic sans ms'),
        ('courier new,courier,monospace', 'courier new'),
        ('georgia,serif', 'georgia'),
        ('lucida sans unicode,lucida grande,sans-serif',
         'lucida sans unicode'),
        ('tahoma,geneva,sans-serif', 'tahoma'),
        ('times new roman,times,serif', 'times new roman'),
        ('trebuchet ms,helvetica,sans-serif', 'trebuchet ms'),
        ('verdana,geneva,sans-serif', 'verdana')])

    formcolor = SelectField("Color", choices=[('#FF0000', 'Red'), ('#000000', 'Black'), ('#800080', 'Purple'),
                                              ('#FFC0CB', 'Pink'), ('#0000FF', 'Blue'),
                                              ('#FFFF00', 'Yellow'), ('#EE82EE', 'Violet'),
                                              ('#FFFFFF', 'White'), ('#008080', 'Teal'),
                                              ('#FFA500', 'Orange'), ('#191970', 'MidnightBlue'),
                                              ('#FF00FF', 'Magenta'), ('#32CD32', 'LimeGreen'),
                                              ('#FFFFE0', 'LightYellow'), ('#FFB6C1', 'LightPink'),
                                              ('#90EE90', 'LightGreen'), ('#ADD8E6', 'LightBlue'),
                                              ('#7CFC00', 'LawnGreen'), ('#FFFFF0', 'Ivory'),
                                              ('#FF69B4', 'HotPink'), ('#008000', 'Green'),
                                              ('#808080', 'Gray'), ('#FFD700', 'Gold'),
                                              ('#FF00FF', 'Fuchsia'), ('#FF1493', 'DeepPink'),
                                              ('#8B0000', 'DarkRed'), ('#006400', 'DarkGreen'),
                                              ('#A9A9A9', 'DarkGray'), ('#00008B', 'DarkBlue'),
                                              ('#DC143C', 'Crimson'), ('#D2691E', 'Chocolate'),
                                              ('#FF7F50', 'Coral'), ('#A52A2A', 'Brown'),
                                              ('#00FFFF', 'Aqua')])
    forminchead = BooleanField("Include Header", default=True)
    formcenter = BooleanField("Center?",default=True)
    formregen = SubmitField("Regnerate")
    formreset = SubmitField("Reset")




