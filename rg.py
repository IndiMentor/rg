from flask import Flask,render_template
from generator import Review

app = Flask(__name__)
TEST_REVIEW=Review('BigMan','This is the tagline','https://indimentor.tk','DEC-2016')
TEST_REVIEW2=Review('LittleMan','This be the tagline','https://indimentor.tk','APR-2016')
allreviews = [ TEST_REVIEW,TEST_REVIEW2,Review('Ano',
                                               'Back and better than ever',
                                               'https://indimentor.tk',
                                               'Apr=2016')]

@app.route('/')
def hello_world():
    return render_template('bbcode.html',
                           reviews=allreviews,
                           reviewheading="Recent Reviews",
                           reviewsep=" *** ")
    # return 'The test review is {} by {}'.format(TEST_REVIEW.tagline,TEST_REVIEW.who)


if __name__ == '__main__':
    app.run()
