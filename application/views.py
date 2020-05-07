from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from application.models import Note
from django.contrib.auth import login, authenticate
from .forms import RegisterForm
from django.shortcuts import render, redirect
from django.template import loader
from django.contrib.auth.decorators import login_required


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


def add_note(request):
    notes = Note.objects.all()

    context = {
        'notes': notes
    }

    return render(request, 'notes/add.html', context=context)