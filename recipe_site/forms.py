from .models import Comment, Tip
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)


class TipForm(forms.ModelForm):
    class Meta:
        model = Tip
        fields = ('tip',)
