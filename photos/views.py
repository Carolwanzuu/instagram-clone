from photos.models import Image, Profile
from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth.models import User
from .forms import SignInForm
from .models import Image, Profile
from django.contrib.auth.decorators import login_required.


# Create your views here.

def welcome(request):
  return render(request,'home.html')

def register(request):
  if request.method == 'POST':
    form = SignInForm(request.POST)
    if form.is_valid():
            form.save()

            for user in User.objects.all():
                 Profile.objects.get_or_create(user=user)

            username = form.cleaned_data.get('username')
            messages.success(request, f'Your Accout has been created for {username}! You can now log in.')
            return redirect('login')
    else:
        form = SignInForm()
    return render(request, 'register.html', {'form':form})


@login_required(login_url='/accounts/login/')
