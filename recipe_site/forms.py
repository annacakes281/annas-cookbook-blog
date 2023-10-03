from .models import Comment, Tip, Contact
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)


class TipForm(forms.ModelForm):
    class Meta:
        model = Tip
        fields = ('tip',)


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'content',)
