from django import forms
from .models import Topic,Comment
class TopicFrom(forms.ModelForm):

    class Meta:
        model = Topic
        exclude = ['user','is_online']

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        exclude = ['user','topic','up','down']

