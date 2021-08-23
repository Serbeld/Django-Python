from django.conf.urls import url
from lectures_app import views

urlpatterns = [
    url(r'^$', views.home, name="home"),
]