from django.test import TestCase
from .forms import CommentForm, TipForm


class TestForms(TestCase):
    # testing for the forms

    def test_comment_field_is_required(self):
        form = CommentForm({'comment': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('comment', form.errors.keys())
        self.assertEqual(form.errors['comment'][0], 'This field is required.')

    def test_tip_field_is_required(self):
        form = TipForm({'tip': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('tip', form.errors.keys())
        self.assertEqual(form.errors['tip'][0], 'This field is required.')
