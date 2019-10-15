from django.urls import path
from django.contrib import admin

from django.conf.urls import url

from django.contrib.auth.views import LoginView
from . import views
from .models import Student
app_name='faculty'

urlpatterns= [
    #homepage

# url(r'^up/$',views.simple_upload,name='s'),

# url(r'^csv/$',views.upform,name='a'),

    # url(r'^regno-autocomplete/$',views.RegisterNumberAutoComplete.as_view(model=Student),name='regno-autocomplete'),
    # url(r'',views.LoginUserView.as_view(), name='login_new'),
    url(r'',views.facultyattendancepage,name="faculty main"),
]