from .models import Comment
from django import forms


# structure of commentform, using model form, and field is what need to be show in the views
#class meta here idenify the beahviour of the form(which to display) and create the instance of the class(with that behaviour)
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
#reference:https://djangocentral.com/creating-comments-system-with-django/