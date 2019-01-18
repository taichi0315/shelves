from django.views import generic
from .models import Post, AppUser
from django.urls import path, reverse_lazy
from django.contrib.auth import views, mixins
from .forms import LoginForm

class IndexView(generic.ListView):
    template_name = 'shelves/index.html'
    context_object_name = 'posted_list'

    def get_queryset(self):
        return Post.objects.order_by('-created_at')

class LoginView(views.LoginView):
    form_class = LoginForm
    template_name = 'shelves/login.html'
