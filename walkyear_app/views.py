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
from django.core.exceptions import ObjectDoesNotExist

from walkyear_app.models import *
from walkyear_app.model_forms import *
from walkyear_app.forms import *

reserved = ["login", "logout", "create", "update"]

def index(request):
    walkers = Walker.objects.all()
    return render(request, "index.html", locals())

def create(request):
    if request.POST and "username" in request.POST:
        username = request.POST["username"]
        if username in reserved:
            return redirect(index)

        walker, created = Walker.objects.get_or_create(username=username)
        if created:
            walker.minutes = 0
            walker.save()

        return redirect(show, username=username)
    return index(request)

def show(request, username):
    try:
        walker = Walker.objects.get(username=username)
        walkers = reversed(Walker.objects.order_by("minutes"))
        return render(request, "show.html", locals())
    except ObjectDoesNotExist:
        return redirect(index)

def update(request):
    if request.POST and "username" in request.POST:
        username = request.POST["username"]
        try:
            walker = Walker.objects.get(username=username)
            if walker.minutes == None:
                walker.minutes = 0
            walker.minutes += int(request.POST["minutes"])
            walker.save()
            return redirect(show, username=username)
        except ObjectDoesNotExist:
            return redirect(index)

    return index(request)




