from django import forms
from .models import AppUser, Post, Profile
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class SignUpForm(UserCreationForm):
    class Meta:
        model = AppUser
        fields = ("username","email", "displayname")
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("sentence",)

class PostCreateForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ("title","comment","rating")

        widgets = {
            "rating": forms.NumberInput(
                attrs={
                    "type":"range",
                    "step":"0.1",
                    "min":"0.0",
                    "max":"5.0",
                    "v-model":"score",
                }
            )
        }

class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("rating","comment")

        widgets = {
            "rating": forms.NumberInput(
                attrs={
                    "type":"range",
                    "step":"0.1",
                    "min":"0.0",
                    "max":"5.0",
                    "v-model":"score",
                }
            )
        }

class BookSearchPostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title",)

        widgets = {
            "title": forms.HiddenInput(
                attrs={
                    "v-model":"book.volumeInfo.title",
                }
            )
        }