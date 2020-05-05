from django.shortcuts import render

# Create your views here.
from application.models import Note


def index(request):
    """View function for home page of site."""

    num_notes = Note.objects.all().count()
    notes = Note.objects.all()

    context = {
        'num_notes': num_notes,
        'notes': notes
    }

    return render(request, 'index.html', context=context)
