from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from main.forms import BookForm
from main.models import Book

# Create your views here.
def show_main(request):
    context = {
        'name': 'Pak Bepe',
        'class': 'PBP A'
    }

    return render(request, 'main.html', context)