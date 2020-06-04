import factory
from application.models import Note

class NoteFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Note
        django_get_or_create = ('title', 'content', 'user')