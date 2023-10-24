from django.shortcuts import render
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect
from django.urls import reverse
from users.forms import *
from django.forms.formsets import formset_factory
from django.forms import inlineformset_factory
from datetime import datetime
from TibAuction import settings
from .models import *
import urllib
import json

# Create your views here.

@login_required
def profile(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    form = ProfileForm(data=request.POST or None, files=request.FILES or None, instance=profile)

    if form.is_valid():
        form = form.save()


    context = {
        "form": form,
        "profile": profile,
    }

    return render(request, "registration/profile.html", context)


@login_required
def profile_detail(request, pk):
    profile = Profile.objects.get(id=pk)
    user = User.objects.get(profile=profile)
    form = UserUpdateForm(data=request.POST or None, instance=user)
    user_subscription = UserSubscription.objects.filter(active=True, profile=profile)

    if request.method == "POST":
        if form.is_valid():
            form.save(commit=False)
            form.save()
            profile.updated_by = request.user
            profile.save()

            messages.success(request, "User updated!")
            return redirect('/settings')

    context = {
        "profile": profile,
        "form": form,
        "user_subscription": user_subscription,
    }

    return render(request, "registration/profile_detail.html", context)


class LoginView(LoginView):
    def form_valid(self, form):
        # form is valid (= correct password), now check if user requires to set own password
        profile = form.get_user().profile
        if form.get_user().profile.customer and not form.get_user().profile.subscribed:
            print("USER NOT SUBSCRIBED")
            messages.error(self.request, 'Your subscription has expired to wateriqcloud.com. Please contact support@wateriqtech.com to renew!')
            return HttpResponseRedirect('/users/accounts/login/')

        if not form.get_user().profile.changed_password:
            self.request.session['user_id'] = form.get_user().id
            print(form.get_user().id)
            return HttpResponseRedirect('/users/reset_password')
        else:
            login(self.request, form.get_user())
            return HttpResponseRedirect('/')
        


