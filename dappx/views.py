# dappx/views.py
import json
import logging
import os

import requests
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from dappx.forms import UserFeedbackInfoForm
from dappx.forms import UserForm
from dappx.forms import UserProfileInfoForm
from dprojx.settings import LOG_DIR

# log config
logging.basicConfig(filename=LOG_DIR + os.sep + 'dappx.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def handler404(request, *args):
    return render(request, 'dappx/404.html')

def handler500(request, *args):
    return render(request, 'dappx/500.html')

def index(request):
    try:
        return render(request, 'dappx/index.html')
    except Exception:
        logging.exception("Exception in index view...")


@login_required
def special(request):
    try:
        return HttpResponse("You are logged in !")
    except Exception:
        pass

@login_required
def user_logout(request):
    try:
        logout(request)
        logging.info("User logged out...")
        return HttpResponseRedirect(reverse('index'))
    except Exception:
        logging.exception("Exception in logout view...")



def register(request):
    try:
        registered = False
        if request.method == 'POST':
            user_form = UserForm(data=request.POST)
            profile_form = UserProfileInfoForm(data=request.POST)
            if user_form.is_valid() and profile_form.is_valid():
                user = user_form.save()
                user.set_password(user.password)
                user.save()
                profile = profile_form.save(commit=False)
                profile.user = user
                if 'profile_pic' in request.FILES:
                    print('found it')
                    profile.profile_pic = request.FILES['profile_pic']
                profile.save()
                registered = True
                logging.info("User registration completed...")
            else:
                print(user_form.errors, profile_form.errors)
        else:
            user_form = UserForm()
            profile_form = UserProfileInfoForm()
        return render(request, 'dappx/registration.html',
                      {'user_form': user_form,
                       'profile_form': profile_form,
                       'registered': registered})
    except Exception:
        logging.exception("Exception in register...")


def user_login(request):
    try:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    logging.info("User auth and logged in...")
                    return HttpResponseRedirect(reverse('index'))
                else:
                    return HttpResponse("Your account was inactive.")
            else:
                print("Someone tried to login and failed.")
                print("They used username: {} and password: {}".format(username, password))
                logging.info("Invalid login credentials...")
                return HttpResponse("Invalid login details given")

        else:
            return render(request, 'dappx/login.html', {})

    except Exception:
        logging.exception("Exception in login view...")


@login_required
def update_profile(request):
    try:
        profile_updated = False
        if request.method == 'POST':
            try:
                profile_form = UserProfileInfoForm(request.POST, request.FILES, instance=request.user.profile)
            except Exception:
                return HttpResponse("You are logged through Social Account !")
            if profile_form.is_valid():
                profile_form.save()
                profile_updated = True
                logging.info("User profile update completed...")
        else:
            try:
                profile_form = UserProfileInfoForm(instance=request.user.profile)
            except Exception:
                return HttpResponse("You are logged in through Social Account !")

        context = {'profile_form': profile_form, 'profile_updated': profile_updated}
        logging.info("User profile updated...")
        return render(request, 'dappx/update_profile.html', context)
    except Exception:
        logging.exception("Exception in update profile...")


@login_required
def feedback(request):
    try:
        submitted = False
        if request.method == 'POST':
            fb_form = UserFeedbackInfoForm(request.POST, request.FILES)
            if fb_form.is_valid():
                feedback = fb_form.save(commit=False)
                feedback.user = request.user
                if 'attachment' in request.FILES:
                    print('found it')
                    feedback.attachment = request.FILES['attachment']
                feedback.save()
                submitted = True
                logging.info("User feedback submission completed...")
            else:
                print(fb_form.errors)
        else:
            fb_form = UserFeedbackInfoForm()
        return render(request, 'dappx/feedback.html',
                      {'fb_form': fb_form,
                       'submitted': submitted})
    except Exception:
        logging.exception("Exception in feedback...")


@login_required()
def news(request):
    try:
        news_api_request = requests.get(
            "http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=6533ff6ff7e644539cb48f5d9888fb1b")
        api = json.loads(news_api_request.content)
        logging.info("News feed generated...")
        return render(request, 'dappx/news.html', {'api': api})
    except Exception:
        logging.exception("Exception in news...")
