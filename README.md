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



