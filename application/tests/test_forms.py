from django.test import TestCase

from application.forms import NoteForm, UpdateNoteForm


class NoteFormTest(TestCase):
    def test_form_title_label(self):
        form = NoteForm()
        self.assertTrue(form.fields['title'])

    def test_form_content_label(self):
        form = NoteForm()
        self.assertTrue(form.fields['content'])

    def test_invalid_form(self):
        form = NoteForm()
        self.assertFalse(form.is_valid())

    def test_invalid_form_title(self):
        form = NoteForm(data={'content': 'content'})
        self.assertFalse(form.is_valid())

    def test_invalid_form_content(self):
        form = NoteForm(data={'title': 'title'})
        self.assertFalse(form.is_valid())

    def test_valid_form(self):
        form = NoteForm(data={'title': 'title', 'content': 'content'})
        self.assertTrue(form.is_valid())


class UpdateNoteFormTest(TestCase):
    def test_form_is_read_label(self):
        form = UpdateNoteForm()
        self.assertTrue(form.fields['is_read'])

    def test_invalid_form(self):
        form = UpdateNoteForm()
        self.assertFalse(form.is_valid())

    def test_valid_form(self):
        form = UpdateNoteForm(data={'is_read': 'on'})
        self.assertTrue(form.is_valid())
