from photos.models import Image, Profile
from django.shortcuts import render


# Create your views here.
def welcome(request):
  return render(request,'home.html')