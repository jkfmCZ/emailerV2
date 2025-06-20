from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import EmailsForm, ContactsForm, MessageForm
from .models import Emails, Contacts, Message
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
import threading
import time
from .logic import start_sender_thread

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # automatické přihlášení po registraci
            return redirect('main')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
@login_required
def conf(request):
    user = request.user
    log = "Login"
    if  user.is_authenticated:
        log = "Logout"
    try:
        connection = Emails.objects.get(user=request.user)
    except Emails.DoesNotExist:
        connection = None

    if request.method == 'POST':
        form = EmailsForm(request.POST, instance=connection)
        if form.is_valid():
            conn = form.save(commit=False)
            conn.user = request.user
            conn.save()
            return redirect('main')
    else:
        form = EmailsForm(instance=connection)

    return render(request, 'conf.html', {'form': form, 'log':log, 'connection_exists': bool(connection)})

@login_required
def msg(request):
    user = request.user
    log = "Login"
    if  user.is_authenticated:
        log = "Logout"
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():

            name = form.cleaned_data['name']
            exists = Message.objects.filter(user=request.user, name=name).exists()
            
            if not exists:
                conn = form.save(commit=False)
                conn.user = request.user
                conn.save()
            else:
                form.add_error('name', 'Tento kontakt již existuje.')
        return redirect('msg')

    else:
        form = MessageForm()
    try:
        msgs = Message.objects.filter(user=request.user).values()
    except: msgs = ""

    return render(request, 'msg.html', {'form': form, 'log':log, 'msgs': msgs})

@login_required
def contacts(request):
    user = request.user
    log = "Login"
    if  user.is_authenticated:
        log = "Logout"
    if request.method == 'POST':
        form = ContactsForm(request.POST, user=request.user)
        if form.is_valid():

            email = form.cleaned_data['email']
            exists = Contacts.objects.filter(user=request.user, email=email).exists()
            
            if not exists:
                conn = form.save(commit=False)
                conn.user = request.user
                conn.save()
            else:
                form.add_error('email', 'Tento kontakt již existuje.')
        return redirect('contacts')

    else:
        form = ContactsForm(user=request.user)


    return render(request, 'contacts.html', {'form': form, 'log':log, 'contacts': Contacts.objects.all().values()})

def tester(request):
    return HttpResponse("Skibidy")





def main(request):
    if not hasattr(start_sender_thread, 'started'):
        start_sender_thread()
        start_sender_thread.started = True
    
    user = request.user
    log = "Login"
    if  user.is_authenticated:
        log = "Logout"

    try:
        contacts = Contacts.objects.filter(user=request.user).values()
    except: contacts = ""
    # for x in  Contacts.objects.filter(user=1):
    #     print(x.message)
    return render(request, "main.html", {'user': user, 'log':log, 'contacts': contacts })
# Create your views here.
