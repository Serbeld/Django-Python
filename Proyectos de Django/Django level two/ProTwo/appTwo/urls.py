from django.conf.urls import url
from django.urls.resolvers import URLPattern 
from appTwo import views

urlpatterns = [ 
    url(r'^$', views.users, name='users'),
]