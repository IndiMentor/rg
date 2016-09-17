from flask import Flask,render_template
from generator import Review

app = Flask(__name__)
TEST_REVIEW=Review('BigMan','This is the tagline','https://indimentor.tk','DEC-2016')
TEST_REVIEW2=Review('LittleMan','This be the tagline','https://indimentor.tk','APR-2016')
allreviews = [
Review('rman9119',
       'Wow',
       'http://independentgirls.com/indiboard/index.php/topic/479532-xxxheather-milf-is-good-for-the-body',
       '42461',
       'xxxHeather'),
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

@app.route('/')
def hello_world():
    return render_template('bbcode.html',
                           reviews=allreviews,
                           reviewheading="Recent Reviews",
                           reviewsep=" *** ",
                           headchar='-')
    # return 'The test review is {} by {}'.format(TEST_REVIEW.tagline,TEST_REVIEW.who)


if __name__ == '__main__':
    app.run()
