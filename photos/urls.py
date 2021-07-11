from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.welcome,name = 'home'),
    url('about/', views.about, name = 'about'),
]