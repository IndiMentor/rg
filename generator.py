"""Generator contains helper functions and classes for generating review bb code"""

__author__ = 'eljefeloco'

class Review:
    """A Review object encapsulates inportant fields"""
    def __init__(self,who,tagline,url,when,reviewof="self"):
        self.who = who
        self.tagline = tagline
        self.url = url
        self.when = when
        self.reviewof = reviewof


def main():

    r1 = Review('Brian','Blew my mind','http://indimentor.tk/','Oct-2016')
    r2 = Review('HipMonster','The Best a Man Can Get','http://indimentor.tk/','Oct-2016')
    r3 = Review('ForeverOrange','WOW!  Meet my new ATF.','http://indimentor.tk/','Oct-2016')
    r4 = Review('WTF','The Most beautiful Girl in the World!','http://indimentor.tk/','Oct-2016')
    r5 = Review('CoolHandLuke','Blew my willy','http://indimentor.tk/','Oct-2016')

    allreviews = []

    allreviews.append(r1)
    allreviews.append(r2)
    allreviews.append(r3)
    allreviews.append(r4)
    allreviews.append(r5)

    for rvw in allreviews:
        print("{} by {}".format(rvw.tagline,rvw.who))

    return

if __name__ == '__main__':
    main()
