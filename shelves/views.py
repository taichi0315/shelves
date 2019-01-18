from django.views import generic
from .models import Post, AppUser
from django.urls import path, reverse_lazy
from django.contrib.auth import views, mixins
from .forms import LoginForm, SignUpForm

class IndexView(generic.ListView):
    template_name = 'shelves/index.html'
    context_object_name = 'posted_list'

    def get_queryset(self):
        return Post.objects.order_by('-created_at')

class LoginView(views.LoginView):
    form_class = LoginForm
    template_name = 'shelves/login.html'

class LogoutView(views.LogoutView, mixins.LoginRequiredMixin):
    template_name = 'shelves/logout.html'

class SignUpView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'shelves/signup.html'
    success_url = reverse_lazy('shelves:login')

class ProfileView(generic.DetailView):
    template_name = 'shelves/profile.html'
    model = AppUser