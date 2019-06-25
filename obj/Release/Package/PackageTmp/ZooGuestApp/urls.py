"""
Definition of urls for ZooGuestApp.
"""

from datetime import datetime
from django.urls import path, include
from django.views.generic.base import TemplateView
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views
admin.autodiscover()


urlpatterns = [
    path('', views.home, name='home'),
    path('map/', views.map, name ='map'),
    path('showTimes/', views.showTimes, name ='showTimes'),
    path('showTimesDetails/', views.showTimesLoop, name ='showTimesDetails'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('feedback/', views.feedback_form, name='feedback'),
    path('home/feedback/', views.feedback_form, name='feedback'),
    path('map/feedback/', views.feedback_form, name='feedback'),
    path('showTimes/feedback/', views.feedback_form, name='feedback'),
    path('contact/feedback/', views.feedback_form, name='feedback'),
    path('pdfMap/feedback/', views.feedback_form, name='feedback'),
    path('feedback/feedback/', views.feedback_form, name='feedback'),
    path('pdfMap/', views.pdfMap, name="pdfMap"),
    path('show/list', views.ShowList.as_view(), name='show_list'),
    path('pushLocation/', views.pushLocation, name="pushLocation"),
    path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
]
