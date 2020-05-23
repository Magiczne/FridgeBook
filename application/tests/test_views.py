from django.contrib.auth.models import User
from django.test import TestCase


class IndexTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='ala', email='ala@makota.com', password='ala-ma-kota-333')
        self.url = '/application/'

    def login(self):
        self.client.login(username='ala', email='ala@makota.com', password='ala-ma-kota-333')

    def test_get_no_login(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/login/?next=/application/')

    def test_get(self):
        self.login()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')


class AddNoteTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='ala', email='ala@makota.com', password='ala-ma-kota-333')
        self.url = '/application/notes/add/'

    def login(self):
        self.client.login(username='ala', email='ala@makota.com', password='ala-ma-kota-333')

    def test_get_no_login(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/login/?next=/application/notes/add/')

    def test_get(self):
        self.login()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'notes/add.html')

    def test_post_no_title(self):
        self.login()
        response = self.client.post(self.url, {'content': 'content'})
        self.assertEqual(response.status_code, 200)
        self.assertFormError(response, 'form', 'title', 'This field is required.')

    def test_post_no_content(self):
        self.login()
        response = self.client.post(self.url, {'title': 'title'})
        self.assertEqual(response.status_code, 200)
        self.assertFormError(response, 'form', 'content', 'This field is required.')

    def test_post(self):
        self.login()
        response = self.client.post(self.url, {'title': 'title', 'content': 'content'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/application/')

        