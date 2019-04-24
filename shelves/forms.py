from django import forms
from .models import AppUser, Post, Profile, Book
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

class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title","rating","comment")

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
class PostDeleteForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ()

class BookCreateForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ("title","book_id","cover_url")

        widgets = {
            "title": forms.HiddenInput(
                attrs={
                    "v-model":"book.volumeInfo.title",
                }
            ),
            "book_id": forms.HiddenInput(
                attrs={
                    "v-model":"book.volumeInfo.industryIdentifiers[0].identifier",
                }
            ),
            "cover_url": forms.HiddenInput(
                attrs={
                    "v-if":"book.volumeInfo.imageLinks !== $0",
                    "v-model":"book.volumeInfo.imageLinks.thumbnail",
                }
            ),
        }