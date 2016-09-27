"""Uses a form to generate an Indi Reviews Excerpt for incusion in your ad / signature / profile
currently only accepts Reviews posted on independentgirls.com



"""
from flask import Flask, render_template, session, request
from models import Review
from forms import ReviewForm, URLForm
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_nav.elements import Navbar, View
from flask_nav import register_renderer
from inverse_render import InverseRenderer  # or wherever you put all of it
import logging
import pickle

nav = Nav()
app = Flask(__name__)
app.secret_key = 'iou98weuyern84hbfrehdsyyds9y8Y98Y98HLFR8YHoiuhjyhoui'
Bootstrap(app)

TEST_REVIEW = Review('BigMan', 'This is the tagline', 'https://indimentor.tk', 'DEC-2016')
TEST_REVIEW2 = Review('LittleMan', 'This be the tagline', 'https://indimentor.tk', 'APR-2016')
allreviews = [
    Review('rman9119', 'Wow',
           'http://independentgirls.com/indiboard/index.php/topic/'
           '479532-xxxheather-milf-is-good-for-the-body',
           '42461', 'xxxHeather'),
    Review('flsailor', 'Amazing Milf', 'http://independentgirls.com/indiboard/index.php/topic/'
           '477279-xxxheather', '42430', 'xxxHeather'),
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


@app.route("/review", methods=('POST', 'GET'))
def withurl():
    logging.info("Hit /review url")
    if 'reviews' not in session:
        logging.info("Checked Session has no reviews in it")
        exist_reviews = []
        json_data = pickle.dumps(exist_reviews)
        session['reviews'] = json_data
        logging.info("created & stored empty seviews %s",json_data)
    else:
        logging.info("Checked session has reviews cookie load it")
        json_data = session['reviews']
        exist_reviews = pickle.loads(json_data)
        logging.debug("Session loaded %s",exist_reviews)

    uform = URLForm()
    # Check which request method was used
    if request.method == "POST":
        logging.info("Was method==POST")
        # Now check which buuton was pressed
        if uform.formreset.data:
            logging.info("Reset pressed")
            # reset pressed.  Wipeout data and cookie
            exist_reviews = []
            json_data = pickle.dumps(exist_reviews)
            session['reviews'] = json_data
            logging.debug("empty session reviews = " + str(json_data))
        elif uform.formregen.data:
            logging.info("Regen was pressed.")
            return render_template(uform.formtheme.data,
                                   form=uform,
                                   reviews=exist_reviews,
                                   reviewheading=uform.rewiewheading.data,
                                   reviewsep=uform.rewiewsep.data,
                                   headchar=uform.headchar.data,
                                   vcolor=uform.formcolor.data.lower(),
                                   vfont=uform.formheadfont.data,
                                   bfont=uform.formbodyfont.data,
                                   incheader=uform.forminchead.data,
                                   vcenter=uform.formcenter.data)
            # Regen was chosen.  Just render w/o creating new review
        else:
            logging.info("Add review was pressed.")
            # addreview was chosen. Validate, create new review & store it
            if uform.validate_on_submit():
                logging.debug("url:%s ", uform.ReviewURL.data)
                new_rvw = Review.from_page(uform.ReviewURL.data)
                exist_reviews.append(new_rvw)
                logging.debug("Resulting review %s",exist_reviews)
                session['reviews'] = pickle.dumps(exist_reviews)
                return render_template(uform.formtheme.data, form=uform, reviews=exist_reviews,
                                       reviewheading=uform.rewiewheading.data,
                                       reviewsep=uform.rewiewsep.data,
                                       headchar=uform.headchar.data,
                                       vcolor=uform.formcolor.data.lower(),
                                       vfont=uform.formheadfont.data,
                                       bfont=uform.formbodyfont.data,
                                       incheader=uform.forminchead.data,
                                       vcenter=uform.formcenter.data)
    # must have been a GET, show the base form view
    logging.info("Was method==GET")
    return render_template('onget.html', form=uform)


@app.route("/price")
def price():
    logging.info("rendering price page")
    return render_template("price.html")


@app.route("/")
def index():
    logging.info("Rendering home")
    return render_template("home.html")


@nav.navigation()
def basicnavbar():
    logging.info("Initialising navbar")
    return Navbar(
        'Indi Tools',
        View('Home', 'index'),
        View('Review Generator', 'withurl'),
        View('Price Generator', 'price'),
    )

nav.init_app(app)
register_renderer(app, 'custom', InverseRenderer)
if __name__ == '__main__':
    logging.basicConfig(
        format='%(asctime)s %(message)s',
        datefmt='%m/%d/%Y %I:%M:%S %p',
        level=logging.DEBUG,
        filename="./rg.log"
    )
    logging.info("*" * 80)
    logging.info("Starting uwsgi app server")
    app.run()
