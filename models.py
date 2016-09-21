"""Generator contains helper functions and classes for generating review bb code"""
from bs4 import BeautifulSoup
import requests

__author__ = 'eljefeloco'


class Review:
    """A Review object encapsulates inportant fields"""
    def __init__(self, who=None, tagline=None, url=None, when=None, reviewof=None):
        self.who = who
        self.tagline = tagline
        self.url = url
        self.when = when
        self.reviewof = reviewof

    @classmethod
    def from_data(cls, who, tagline, url, when, reviewof=None):
        return cls(who, tagline, url, when, reviewof)

    @classmethod
    def from_page(cls, page_url):


        the_page = requests.get(page_url)
        bs = BeautifulSoup(the_page.content,"html.parser")

        # scrape the data
        who = bs.find(itemprop="creator name").get_text(strip=True)
        tagline = bs.find("h1").get_text(strip=True, separator=u" ")
        # url = page_url
        when = bs.find(itemprop="commentTime")['title']
        reviewof = ""
        url = bs.find("link", {'rel':'canonical'}).attrs.get('href', None)

        return cls(who, tagline, url, when, reviewof)


def main():

    r1 = Review('Brian', 'Blew my mind', 'http://indimentor.tk/', 'Oct-2016')
    r2 = Review('HipMonster', 'The Best a Man Can Get', 'http://indimentor.tk/', 'Oct-2016')
    r3 = Review('ForeverOrange', 'WOW!  Meet my new ATF.', 'http://indimentor.tk/', 'Oct-2016')
    r4 = Review('WTF', 'The Most beautiful Girl in the World!', 'http://indimentor.tk/', 'Oct-2016')
    r5 = Review('CoolHandLuke', 'Blew my willy', 'http://indimentor.tk/', 'Oct-2016')

    allreviews = []

    allreviews.append(r1)
    allreviews.append(r2)
    allreviews.append(r3)
    allreviews.append(r4)
    allreviews.append(r5)

    for rvw in allreviews:
        print("{} by {}".format(rvw.tagline, rvw.who))

    return

if __name__ == '__main__':
    main()
