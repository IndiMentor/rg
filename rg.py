"""Uses a form to generate an Indi Reviews Excerpt for incusion in your ad / signature / profile
currently only accepts Reviews posted on independentgirls.com

Developer Notes:

To add a new template:
    1. Write a new jinja template that extends bbcode.html
    2. Write a block called thethebbcode which includes the required bbcode
    3. You will have access to:
        reviews - A list of all the reviews
        headchar
        reviewheading
        reviewsep
    4. Add your theme name and theme filename to the formtheme select field of UrlForm
       in forms.py
    5. That's all.
"""
from flask import Flask,render_template,session, request
from models import Review
from forms import ReviewForm, URLForm
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_nav.elements import Navbar, View
from flask_nav import register_renderer
from inverse_render import InverseRenderer  # or wherever you put all of it
import pickle

nav = Nav()
app = Flask(__name__)
app.secret_key = 'iou98weuyern84hbfrehdsyyds9y8Y98Y98HLFR8YHoiuhjyhoui'
Bootstrap(app)

TEST_REVIEW = Review('BigMan','This is the tagline','https://indimentor.tk','DEC-2016')
TEST_REVIEW2 = Review('LittleMan','This be the tagline','https://indimentor.tk','APR-2016')
allreviews = [
    Review('rman9119','Wow',
           'http://independentgirls.com/indiboard/index.php/topic/479532-xxxheather-milf-is-good-for-the-body',
           '42461','xxxHeather'),
    Review('flsailor', 'Amazing Milf', 'http://independentgirls.com/indiboard/index.php/topic/477279-xxxheather',
           '42430', 'xxxHeather'),
    Review('avgjoe', 'A Real Dream',
           'http://independentgirls.com/indiboard/index.php/topic/473840-xxxheather', '42430', 'xxxHeather'),
    Review('JDBones', 'Totally Blown Away ',
           'http://independentgirls.com/indiboard/index.php/topic/464551-xxxheather-oops-i-did-it-again',
           '42339', 'xxxHeather'),
    Review('majiquer', 'An Absolute Doll',
           'http://independentgirls.com/indiboard/index.php/topic/463674-xxxheather-an-absolute-doll',
           '42339', 'xxxHeather'),
    Review('JDBones', 'Oral Assault',
           'http://independentgirls.com/indiboard/index.php/topic/458185-amyheathers-new-protege', '42309',
           'xxxHeather'),
    Review('monger48', 'Heather Is A Freak!',
           'http://independentgirls.com/indiboard/index.php/topic/456876-xxxheather', '42309', 'xxxHeather'),
    Review('miamivice51', 'A Kid Waiting For Christmas',
           'http://independentgirls.com/indiboard/index.php/topic/451367-xxxheather-mariposa69-xxx-x-22',
           '42248', 'xxxHeather'),
    Review('tres_huecos', ' Best Bbbjs I Have Ever Had',
           'http://independentgirls.com/indiboard/index.php/topic/451035-xxxheather', '42248', 'xxxHeather'),
    Review('miamivice51', 'Omg, Jackpot!!!!!',
           'http://independentgirls.com/indiboard/index.php/topic/449885-xxxheather', '42248', 'xxxHeather'),
    Review('bigk621', 'She Rocks!',
           'http://independentgirls.com/indiboard/index.php/topic/447542-xxxheather-rated-appropiately',
           '42217', 'xxxHeather'),
    Review('JDBones', 'Great Oral Skills !!',
           'http://independentgirls.com/indiboard/index.php/topic/446625-xxxheather-great-oral-skills',
           '42217', 'xxxHeather'),
    Review('JDBones', 'What A Way To Start The Day',
           'http://independentgirls.com/indiboard/index.php/topic/442698-xxxheather-michellenyc-have-a'
           '-playdate',
           '42186', 'xxxHeather'),
    Review('vanhalen84', 'Wow What A Great Time..........',
           'http://independentgirls.com/indiboard/index.php/topic/424744-xxxheatherxxx', '42064',
           'xxxHeather'),
    Review('Clark360', 'Holy Fuck! ',
           'http://independentgirls.com/indiboard/index.php/topic/411105-xxxheather', '41944', 'xxxHeather'),
    Review('Altacocker', 'Back And Better Than Ever',
           'http://independentgirls.com/indiboard/index.php/topic/401525-xxxheather', '41883', 'xxxHeather'),
    ]


@app.route("/review",methods=('POST','GET'))
def withurl():

    if 'reviews' not in session:
        exist_reviews = []
        json_data = pickle.dumps(exist_reviews)
        session['reviews'] = json_data
    else:
        json_data = session['reviews']
        exist_reviews = pickle.loads(json_data)

    uform = URLForm()
    # Check which request method was used
    if request.method == "POST":
        # Now check which buuton was pressed
        if uform.formreset.data:
            # reset pressed.  Wipeout data and cookie
            exist_reviews = []
            json_data = pickle.dumps(exist_reviews)
            session['reviews'] = json_data
        elif uform.formregen.data:
            # Regen was chosen.  Just render w/o creating new review
            return render_template(uform.formtheme.data,
                                   form=uform,
                                   reviews=exist_reviews,
                                   reviewheading=uform.rewiewheading.data,
                                   reviewsep=uform.rewiewsep.data,
                                   headchar=uform.headchar.data)
        else:
            # addreview was chosen. Validate, create new review & store it
            if uform.validate_on_submit():
                new_rvw = Review.from_page(uform.ReviewURL.data)
                exist_reviews.append(new_rvw)
                session['reviews'] = pickle.dumps(exist_reviews)
                return render_template(uform.formtheme.data,form=uform,reviews=exist_reviews,
                                       reviewheading=uform.rewiewheading.data,
                                       reviewsep=uform.rewiewsep.data,
                                       headchar=uform.headchar.data)
    # must have been a GET, show the base form view
    return render_template('onget.html',form=uform)


@app.route("/price")
def price():
    return render_template("price.html")


@app.route("/")
def index():
    return render_template("home.html")


@nav.navigation()
def basicnavbar():
    return Navbar(
        'Indi Tools',
        View('Home', 'index'),
        View('Review Generator','withurl'),
        View('Price Generator','price'),
    )

nav.init_app(app)
if __name__ == '__main__':
    register_renderer(app, 'custom', InverseRenderer)
    app.run()
