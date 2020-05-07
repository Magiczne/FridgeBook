from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import login, authenticate
from .forms import RegisterForm
from django.shortcuts import render, redirect
from django.template import loader
from django.contrib.auth.decorators import login_required

from application.models import Note
from application.forms import NoteForm


@login_required(login_url='/login/')
def index(request):
    """View function for home page of site."""

    num_notes = Note.objects.all().count()
    notes = Note.objects.all()

    context = {
        'num_notes': num_notes,
        'notes': notes
    }

    return render(request, 'index.html', context=context)


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/application/')
    else:
        form = RegisterForm()

    template = loader.get_template('register.html')
    context = {'form': form}
    return HttpResponse(template.render(context, request))


@login_required(login_url='/login/')
def add_note(request):
    if request.method == 'POST':
        note = Note()
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            note.user = request.user
            note = form.save(commit=False)
            note.save()
            return redirect('/application/')
    else:
        form = NoteForm()
    
    context = {'form': form}
    return render(request, 'notes/add.html', context=context)