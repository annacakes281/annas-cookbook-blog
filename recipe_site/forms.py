from .models import Comment, Tip, ContactMe
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)


class TipForm(forms.ModelForm):
    class Meta:
        model = Tip
        fields = ('tip',)


class ContactMeForm(forms.ModelForm):
    class Meta:
        model = ContactMe
        fields = ('name', 'email', 'content',)
