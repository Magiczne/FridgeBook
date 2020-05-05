from django.test import TestCase

from application.models import Note


class NoteTestCase(TestCase):
    def setUp(self):
        Note.objects.create(content="note")
        Note.objects.create(content="new note")
        Note.objects.create(content="newest note")

    def test_find_note_by_content(self):
        note = Note.objects.filter(content="note").first()
        self.assertEqual(note.content, "note")

    def test_notes_ordering(self):
        notes = Note.objects.all()
        self.assertEqual(notes[0].content, "newest note")
        self.assertEqual(notes[1].content, "new note")
        self.assertEqual(notes[2].content, "note")
