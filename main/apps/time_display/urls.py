from django.conf.urls import url
from . import views           # This line is new!


urlpatterns = [
    url(r'^displaytime/$', views.index),     # This line has changed!
]
