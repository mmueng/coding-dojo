from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages
import re
import bcrypt
import datetime
from django.utils import timezone


def index(request):
    if not valid_login(request):
        return redirect('/')
    context = {
        'live_user': User.objects.get(id=request.session['live_user']),
        'all_jobs': Job.objects.filter(),
        'all_users': User.objects.all(),
    }
    return render(request, 'belt_app/index.html', context)


def new(request):
    if not valid_login(request):
        return redirect('/')

    return render(request, 'belt_app/new.html')


def add_job(request):
    if not valid_login(request):
        return redirect('/')
    errors = Job.objects.job_validatoradd(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, key)
        return redirect('/jobs/new')

    else:
        live_user = User.objects.get(id=request.session['live_user'])
        # cat = []
        cat = request.POST.getlist('category')
        # cat = request.POST['category']
        cat2 = request.POST.getlist('category2')
        cat3 = request.POST.getlist('category3')
        # request.POST.getlist('checks')
        # if cat is '':
        #     cat = ' '
        # cat1 = request.POST['category']
        # cat = request.POST.getall('category')
        # cat2 = request.POST.getall('category2')
        # cat3 = request.POST.getall('category3')
        # cat = request.POST['category']
        # cat2 = request.POST['category2']
        # cat3 = request.POST['category3']
        print('*'*10, cat, cat2, cat3)
        # cat = str(cat1) + str(cat2) + str(cat3)
        # cat2 = cat2
        # cat3 = cat3
        # if cat2[0] is '':
        #     cat2[0] = '.'

        # if cat is []:
        #     cat = ''

        Job.objects.create(
            title=request.POST['title'], desc=request.POST['desc'], location=request.POST['location'], other=request.POST['other'],  category=cat, category2=cat2, category3=cat3, creator=live_user).job_user.add(live_user)
        return redirect('/jobs')


def show(request, jobID):
    if not valid_login(request):
        return redirect('/')
    cat = Job.objects.get(id=jobID)
    print('*'*10, cat.category)
    b = str(cat.category)[1:-1]
    a = b.strip("\'")

    c = str(cat.category2)[1:-1]
    d = c.strip("\'")

    e = str(cat.category3)[1:-1]
    f = e.strip("\'")
    print(a)
    context = {
        'live_user': User.objects.get(id=request.session['live_user']),
        'job': Job.objects.get(id=jobID),
        'joob': Job.objects.get(id=jobID).category,
        'a': a,
        'd': d,
        'f': f,
    }
    return render(request, 'belt_app/show.html', context)


def edit(request, jobID):
    if not valid_login(request):
        return redirect('/')
    context = {
        'live_user': User.objects.get(id=request.session['live_user']),
        'job': Job.objects.get(id=jobID),
    }
    return render(request, 'belt_app/edit.html', context)


def process_edit(request, jobID):
    if not valid_login(request):
        return redirect('/')
    errors = Job.objects.job_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, key)
        return redirect(f'/jobs/{jobID}/edit')
    else:
        job = Job.objects.get(id=jobID)
        job.title = request.POST['title']
        job.desc = request.POST['desc']
        job.location = request.POST['location']
        # job.other = request.POST['other']
        # job.category = request.POST['category']

        job.save()
    return redirect('/jobs')


def join(request, jobID):
    if not valid_login(request):
        return redirect('/')
    live_user = User.objects.get(id=request.session['live_user'])
    job = Job.objects.get(id=jobID)
    job.job_user.add(live_user)
    return redirect('/jobs')


def giveup(request, jobID):
    if not valid_login(request):
        return redirect('/')
    live_user = User.objects.get(id=request.session['live_user'])
    job = Job.objects.get(id=jobID)
    job.job_user.remove(live_user)
    return redirect('/jobs')


def delete(request, jobID):
    if not valid_login(request):
        return redirect('/')
    live_user = User.objects.get(id=request.session['live_user'])
    job = Job.objects.get(id=int(jobID))
    if live_user.id == job.creator.id:
        job.delete()
    return redirect('/jobs')


def delete2(request, jobID):
    if not valid_login(request):
        return redirect('/')
    live_user = User.objects.get(id=request.session['live_user'])
    job = Job.objects.get(id=int(jobID))
    job.delete()
    return redirect('/jobs')

# def logout(request):  # logout
#     # if not valid_login(request):
#     #     return redirect('/')
#     request.session.clear()
#     return redirect('/')


def valid_login(request):
    if 'live_user' in request.session:
        return True
    return False
