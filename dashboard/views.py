from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from dashboard.models import *
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail

from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm

from django.contrib import messages

import requests
import json



@login_required
def dashboard(request):
    users = User.objects.all()

    return render(request, 'TibAuction/dashboard.html')





