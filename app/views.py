"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render, render_to_response
from django.http import HttpRequest, HttpResponse
from .forms import FeedbackForm
from django.db import models
from app.models import *
from django.views.generic import View, ListView
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.forms.models import model_to_dict


def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def map(request):
    """Renders the map page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/map.html',
        {
            'title':'map',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def pdfMap(request):
    """Renders the map page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/pdfMap.html',
        {
            'title':'map',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )
def feedback_form(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
 
        if form.is_valid():
            form.save()
            return render(request, 'app/thanks.html')
    else:
        form = FeedbackForm()
    return render(request, 'app/feedback_form.html', {'form': form})


def default_map(request):
    # TODO: move this token to Django settings from an environment variable
    # found in the Mapbox account settings and getting started instructions
    # see https://www.mapbox.com/account/ under the "Access tokens" section
    mapbox_access_token = 'pk.my_mapbox_access_token'
    return render(request, 'app/map2.html', {'mapbox_access_token': mapbox_access_token})


def showTimes(request):
    """Renders the showTimes page."""
    assert isinstance(request, HttpRequest)
    showTimes = Show.objects.all();
    return render( request,'app/showTimes.html',{'showTimes':showTimes}
    )

def showTimesLoop(request):
    times = Show.objects.all();
    return render_to_response('app/showTimesDetails.html', {'times':times} )

def pushLocation(request):
    locations = Location.objects.all();
    assert isinstance(request, HttpRequest)
    return render_to_response('app/pushLocation.html', {'locations':locations} )


class ShowList(ListView):
    def get(self, request):
        shows =list(Show.objects.all().values('showTime', 'showName', 'showMessage'))
        data = dict()
        data['shows'] = shows
        

        return JsonResponse(data)

class ShowLocationList(ListView):
    def get(self, request):
        shows =list(Show.objects.all().values('showLong', 'showLat'))
        data = dict()
        data['shows'] = shows
        

        return JsonResponse(data)

class PopupLocationList(ListView):
    def get(self, request):
        shows =list(PopupLocation.objects.all().values('name','message','long','lat'))
        data = dict()
        data['shows'] = shows
        

        return JsonResponse(data)