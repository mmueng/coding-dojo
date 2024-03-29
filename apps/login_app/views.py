from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages
import re
import bcrypt
import datetime
from django.utils import timezone


def index(request):
    return render(request, 'login_app/index.html')


def registration(request):

    if request.POST['form'] == 'register':
        errors = User.objects.basic_validator(request.POST)
        if len(errors) > 0:

            for key, value in errors.items():
                messages.error(request, value, key)
            return redirect('/')
        else:
            if request.method == 'POST':
                password = request.POST['password']
                pw_hash = bcrypt.hashpw(
                    password.encode(), bcrypt.gensalt())  # create the hash
                print(pw_hash)
                live_user = User.objects.create(
                    first_name=request.POST['first_name'], last_name=request.POST['last_name'], birthday=request.POST['birthday'], email=request.POST['email'], password=pw_hash)
                request.session['live_user'] = live_user.id
                return redirect("/jobs")


def login(request):
    # if not valid_login(request):
    #     return redirect('/')
    if request.POST['form'] == 'login':
        errors = User.objects.login_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value, key)
            return redirect('/')
        else:
            user = User.objects.filter(email=request.POST['email'])
            if user:
                logged_user = user[0]
                if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
                    request.session['live_user'] = logged_user.id
                    return redirect('/jobs')
            messages.error(request, 'login Fail ')
    return redirect("/")


# def logout(request):  # logout
#     if not valid_login(request):
#         return redirect('/')
#     del request.session['live_user']
#     return redirect('/')

# def logout(request):
#     if 'live_user' not in request.session:
#         return redirect('/')
#     del request.session['live_user']

def logout(request):  # logout

    request.session.clear()

    return redirect('/')


def valid_login(request):
    if 'live_user' in request.session:
        return True
    return False
