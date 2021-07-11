from django import forms

class SignInForm(forms.Form):
    your_name = forms.CharField(label='First Name',max_length=30)
    email = forms.EmailField(label='Email')
class PostForm(forms.Form):
    image = forms.ImageField()
    image_name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control","placeholder": "Image Name"}))
    image_caption = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control","placeholder": "Image Caption"}))

class CommentForm(forms.Form):
    body = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control","placeholder": "Leave a comment!"}))