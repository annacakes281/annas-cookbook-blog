from django.test import TestCase


class TestViews(TestCase):

    def test_get_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')  # Failed

    def test_get_view_recipe_page(self):
        response = self.client.get('recipe/<slug:slug>/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'view_recipe.html')  # Failed

    # def test_get_contact_page(self):

    # def test_get_search_page(self):

    # def test_get_accounts_page(self):

    # def test_post_recipe(self):

    # def test_post_comment(self):

    # def test_post_tip(self):

    # def test_like_recipe(self):
