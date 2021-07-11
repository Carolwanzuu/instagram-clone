from photos.models import Image, Profile, Comment
from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect
from .forms import SignInForm,PostForm,CommentForm
from .models import Image, Profile
from django.contrib.auth.decorators import login_required


# Create your views here.
def registerPage(request):
    context = {}
    return render(request,'registration/registration_form.html', context)

def loginPage(request):
    context = {}
    return render(request,'registration/login.html', context)


def home(request):
    post = Image.objects.all()

    context={
        'posts' : post,
    }

    return render(request, 'home.html',context)


def about(request):
    return render(request, 'about.html', {'title': 'About'})

@login_required
@csrf_protect
def add_post(request):
    form = PostForm(request.POST,request.FILES)
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            post = Image(
                image = form.cleaned_data["image"],
                name = form.cleaned_data["name"],
                caption = form.cleaned_data["caption"],
                author = request.user
            )
            
            post.save()

            name = form.cleaned_data.get('name')
            messages.success(request, f'Your post has been created for {name} !')
            return redirect('home')
    else:
        form = PostForm()

    return render(request, 'addPost.html',{'form': form})

@login_required
@csrf_protect
def post_detail(request, pk):
    post = Image.objects.get(pk=pk)
    user = request.user
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author= user,
                body=form.cleaned_data["body"],
                post=post
            )
            comment.save()

    comments = Comment.objects.filter(post=post).order_by('-created_on')
    context = {
        "post": post,
        "comments": comments,
        "form": form,
    }

    return render(request, "addPost.html", context)

@login_required
def like(request, pk):
    post = Image.objects.get(pk=pk)
    post.likes+=1
    post.save()
    return redirect('home')
