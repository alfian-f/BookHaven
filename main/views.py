from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from main.forms import BookForm
from main.models import Book
import csv
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group, User
from django.contrib import messages  
from django import forms


class RegisterForm(UserCreationForm):
    email = forms.EmailField(label = "Email")
    fullname = forms.CharField(label = "Full")

    class Meta:
        model = User
        fields = ("username", "fullname", "email", )
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].help_text = None
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None
        
    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        first_name, middle_name, last_name = self.cleaned_data["fullname"].split()
        user.first_name = first_name
        user.last_name = last_name
        user.middle_name = middle_name
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
    

    
# Create your views here.
def show_main(request):
    context = {
        'name': 'Pak Bepe',
        'class': 'PBP A'
    }

    return render(request, 'main.html', context)

def top(request):
    x = []
    with open('archive/Books.csv') as file:
        csv_reader = csv.DictReader(file)

        for line in csv_reader:
            x += [line['Book-Title']]
    context = {"Titles": x[:10]}
    return render(request, "top.html", context)

def library(request):
    context = {}
    return render(request, "library.html", context)

def booklist(request):
    context = {}
    return render(request, "booklist.html", context)

def register(request):
    form = RegisterForm()

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main')
    context = {'form':form}
    return render(request, 'register.html', context)