from django.db import models
from django.contrib.auth.models import User

# # Create your models here
class Image(models.Model):
    image=models.ImageField(upload_to='profile_pics')
    name=models.CharField(max_length=100)
    caption=models.TextField()
    profile= models.ForeignKey(User, on_delete=models.CASCADE)
    likes=models.IntegerField(null=True, default=0)
    comments=()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(default='Bio...📰', max_length=100)

    def __str__(self):
        return f'{self.user.username} Profile'

# class Post(models.Model):
#     image = models.ImageField(upload_to='post_images')
#     image_name = models.CharField(max_length=100)
#     image_caption = models.TextField(max_length=300)
#     created_on = models.DateTimeField(auto_now_add=True)
#     last_modified = models.DateTimeField(auto_now=True)
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
#     likes = models.IntegerField(null=True, default=0)

#     def __str__(self):
#         return self.image_name

# class Comment(models.Model):
#     body = models.TextField()
#     created_on = models.DateTimeField(auto_now_add=True)
#     post = models.ForeignKey('Post', on_delete=models.CASCADE)
#     author = models.ForeignKey(User, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.post
