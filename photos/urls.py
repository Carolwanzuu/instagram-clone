from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.welcome,name = 'home'),
    url('about/', views.about, name = 'about'),
    url('add_post/', views.about, name = 'add_post'),
    url('<int:pk>/', views.about, name = 'post_detail'),
    url('<int:pk>/', views.about, name = 'likes'),
]