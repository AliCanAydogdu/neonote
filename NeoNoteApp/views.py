from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .models import Places, Group
from .forms import (
    UserForm, GroupForm, PlacesForm
)
from datetime import datetime

import geocoder
import numpy as np
import json

def view_about(request):
    return render(request, 'about.html')

def index(request):
    if not request.user.is_authenticated:
        return render(request, 'welcome.html')
    else:
        user = request.user
        place_adds = Places.objects.all().values('address', 'group')
        groups = Group.objects.all()

        lats_longs = []

        for i in place_adds:
            lat,long = location_with_geopy(i["address"])
            group_name = groups.get(id=i["group"])
            group_name = str(group_name)
            new = []
            new.append(lat)
            new.append(long)
            new.append(group_name)
            lats_longs.append(new)

        #so that template doesn't get as string, but as a list
        json_data= json.dumps(lats_longs)
        # lats_longs = np.array(lats_longs)

        context = {
            "user": user,
            "lats_longs": json_data,
            "place_adds":place_adds,
        }
        return render(request, 'index.html', context)

def view_places(request):
    gp = Group.objects.get(user=request.user)
    group_name = gp.group_name

    user_places = Places.objects.filter(user=request.user)
    group_places = Places.objects.filter(group__group_name=group_name).exclude(user=request.user)

    # images = user_places
    context = {
        "user_places": user_places,
        "group_places":group_places,
    }
    return render(request, 'places.html', context)

def new_place(request):
    form = PlacesForm(request.POST or None, request.FILES or None)
    gp = Group.objects.get(user=request.user)

    if form.is_valid():
        n = form.save(commit=False)
        n.date_added =  datetime.now()
        n.user = request.user
        n.group = gp
        img = form.cleaned_data['img']
        form.save()
        return redirect('/NeoNoteApp/places')

    context = {
        "form": form,
    }
    return render(request, 'new_place.html', context)


def sign_up(request):
    user_form = UserForm(request.POST or None)
    group_form = GroupForm(request.POST or None)

    if user_form.is_valid() and group_form.is_valid():
        user = user_form.save(commit=False)
        username = user_form.cleaned_data['username']
        password = user_form.cleaned_data['password']
        user.set_password(password)
        user_form.save()

        user_group = group_form.save(commit=False)
        user_group.user = user_form.save(commit=False)
        user_group.save()

        user = authenticate(username=username, password=password)

        if user is not None:
            return redirect('/NeoNoteApp')

    context = {
        "user_form": user_form,
        "group_form": group_form,
    }
    return render(request, 'signup.html', context)



def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/NeoNoteApp')
            else:
                return render(request, 'login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'login.html', {'error_message': 'Invalid login. Please try again.'})
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return redirect('/NeoNoteApp')


def view_profile(request):
    user = request.user
    group_ = Group.objects.get(user=request.user)
    places_ = Places.objects.filter(user=request.user)
    no_visited_places = len(places_)

    context = {
        "user": user,
        "group":group_,
        "no_visited_places":no_visited_places,
    }
    return render(request, 'profile.html', context)


def location_with_geopy(address):
    g = geocoder.osm(address)
    x_lat = g.osm["x"]
    y_long = g.osm["y"]
    return (x_lat, y_long)
    # locator = Nominatim(user_agent="myGeocoder")
    # location = locator.geocode(address)
    #
    # print("Latitude = {}, Longitude = {}".format(location.latitude, location.longitude))
