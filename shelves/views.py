from django.views import generic
from .models import Post, AppUser, Profile
from django.urls import path, reverse_lazy
from django.shortcuts import resolve_url
from django.contrib.auth import views, mixins
from .forms import LoginForm, SignUpForm, ProfileUpdateForm, PostCreateForm
import requests, json

class IndexView(generic.ListView):
    template_name = 'shelves/index.html'
    context_object_name = 'posted_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cover = {}
        for post in context["object_list"]:
            req_url = 'https://www.googleapis.com/books/v1/volumes?q='+ post.title
            response = requests.get(req_url)
            dic = response.json()
            cover[post.title] = dic["items"][0]["volumeInfo"]["imageLinks"]["thumbnail"]
        print(cover)
        context['cover_dic'] = cover

        return context

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

class ProfileUpdateView(mixins.UserPassesTestMixin, generic.UpdateView):
    raise_exception = False

    model = Profile
    form_class = ProfileUpdateForm
    template_name = 'shelves/profile_update.html'

    def test_func(self):
        user = self.request.user
        return user.pk == self.kwargs['pk'] or user.is_superuser

    def get_success_url(self):
        return resolve_url('shelves:profile', pk=self.kwargs['pk'])

class PostCreateView(generic.CreateView, mixins.UserPassesTestMixin):
    form_class = PostCreateForm
    success_url = reverse_lazy('shelves:index')
    template_name = 'shelves/post_create.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)