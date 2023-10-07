from django.test import TestCase
from .forms import CommentForm, TipForm


class TestForms(TestCase):

    def test_comment_field_is_required(self):
        form = CommentForm({'comment': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('comment', form.errors.keys())
        self.assertEqual(form.errors['comment'][0], 'This field is required.')

    def test_comment_fields_match_in_form_metaclass(self):
        form = CommentForm()
        self.assertEqual(form.Meta.fields, ['comment'])  # shows as failed

    def test_tip_field_is_required(self):
        form = TipForm({'tip': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('tip', form.errors.keys())
        self.assertEqual(form.errors['tip'][0], 'This field is required.')

    def test_tip_fields_match_in_form_metaclass(self):
        form = TipForm()
        self.assertEqual(form.Meta.fields, ['tip'])  # shows as failed
