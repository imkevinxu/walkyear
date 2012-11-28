from django import forms
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core import serializers
from django.core.context_processors import csrf
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect
from coffin.shortcuts import render_to_response, get_object_or_404, render, \
    redirect
from django.template import loader, RequestContext
from django.views.decorators.csrf import csrf_exempt

from walkyear_app.models import *
from walkyear_app.model_forms import *
from walkyear_app.forms import *

def index(request):
    walkers = Walker.objects.all()
    return render(request, "index.html", locals())

def create(request):
    if request.POST and "username" in request.POST:
        username = request.POST["username"]
        walker, created = Walker.objects.get_or_create(username=username)
        if created:
            walker.save()

        return redirect(show, username=username)
    return index(request)

def show(request, username):
    walker = Walker.objects.get(username=username)

    return render(request, "show.html", locals())