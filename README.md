## Indi Tools

### Adding a new template to the review generator

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

TODO:

* Make video showing usage max 1 min.
* Description of how to use incorporated into web page
* ~~Research how to deploy on nginx~~
* ~~Uninstall bbcode~~
* ~~Fix-up validation so if can't get review info fail url~~
* ~~Add Highlight color field~~
* ~~Add Font field both based on values permitted by indi~~
* indimentor intropost
* ~~easyengine setup inditools.tk~~
* ~~Strip out ?blahblah from urls~~
* ~~check if / how urls can be normalized~~
*     ~~<link id="ipsCanonical" rel="canonical"~~ 
~~href="http://independentgirls.com/indiboard/index
.php/topic/459542-pp-yani/"/>~~
* ~~Have theme's incorporate color & font fields~~
* ~~Intro text for home page~~
* ~~Don't show header option~~
* ~~Add center option.~~


### Later versions

* Render bbcode ina seperate template that is written to a string
insert this string into web page and have converted to html by
bbcode so have a preview as well.
* Seperate out add review into two steps fetching review info, and 
adding review.  This would enable adding review info to form so they 
could pver-ride things like tagline etc. before adding review to bbcode
* Replace select list for colors on urlform with a color picker
* Replace quick form with handcode bootstrap form
* Make session use s 30-day cookie so info retained if they accidentally
close the browser
* put search for reviews into the app so they don't have to cut 
switch apps, paste etc

### Theme's

1. Wrapper for signatures
2. Inline for use in ads
3. Centered Column
