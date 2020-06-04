from django.contrib.auth.models import User
from django.test import TestCase

from application.models import Note


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

        
class EditNoteTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='ala', email='ala@makota.com', password='ala-ma-kota-333')
        self.url = '/application/notes/edit/1'
        self.note = Note.objects.create(title='new note', content='note content', user=self.user)

    def login(self):
        self.client.login(username='ala', email='ala@makota.com', password='ala-ma-kota-333')

    def login_as_different(self):
        user = User.objects.create_user(username='ola', email='ola@makota.com', password='securePass343')
        self.client.login(username='ola', email='ola@makota.com', password='securePass343')

    def test_get_no_login(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/login/?next=/application/notes/edit/1')

    def test_get_different_login(self):
        self.login_as_different()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/application/')

    def test_post_no_note(self):
        self.login()
        response = self.client.post('/application/notes/edit/100')
        self.assertEqual(response.status_code, 404)

    def test_post(self):
        self.login()
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, 200)

    def test_post_no_title(self):
        self.login()
        response = self.client.post(self.url, {'title': ''})
        self.assertEqual(response.status_code, 200)
        self.assertFormError(response, 'form', 'title', 'This field is required.')

    def test_post_no_content(self):
        self.login()
        response = self.client.post(self.url, {'content': ''})
        self.assertEqual(response.status_code, 200)
        self.assertFormError(response, 'form', 'content', 'This field is required.')

    def test_post_with_new_value(self):
        self.login()
        response = self.client.post(self.url, {'title': 'new note title', 'content': 'new note content'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/application/')

        note = Note.objects.get(id=1)
        self.assertEqual(note.title, 'new note title')
        self.assertEqual(note.content, 'new note content')
        self.assertEqual(note.user, self.user)
