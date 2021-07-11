from django.conf.urls import url
from . import views

urlpatterns=[
    url('register/', views.registerPage, name = 'register'),
    url('register/', views.loginPage, name = 'login'),

    url('^$',views.home,name = 'home'),
    url('^about/', views.about, name = 'about'),
    url('^add_post/', views.about, name = 'add_post'),
    url('^<int:pk>/', views.about, name = 'post_detail'),
    url('^<int:pk>/', views.about, name = 'likes'),
]