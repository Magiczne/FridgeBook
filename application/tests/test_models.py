from django.contrib.auth.models import User
from django.db.models import deletion
from django.test import TestCase

from application.models import Note


class NoteTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='Test user', email='test@example.com', password='secret')
        self.notes = [
            Note.objects.create(title='note 1', content='note 1 content', user=self.user),
            Note.objects.create(title='note 2', content='note 2 content', user=self.user),
            Note.objects.create(title='note 3', content='note 3 content', user=self.user)
        ]

    def test_find_note_by_content(self):
        note = Note.objects.get(content=self.notes[0].content)

        self.assertEqual(note.content, self.notes[0].content)

    def test_find_note_by_title(self):
        note = Note.objects.get(title=self.notes[1].title)

        self.assertEqual(note.title, self.notes[1].title)

    def test_user_removal_should_fail_if_he_has_notes(self):
        with self.assertRaises(deletion.ProtectedError):
            self.user.delete()
