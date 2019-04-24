from django.views import generic
from django.db.models import Case, When
from django.db import transaction
from .models import Post, AppUser, Profile, RecommendUser, Book
from django.urls import path, reverse_lazy
from django.shortcuts import resolve_url
from django.http import HttpResponseRedirect
from django.contrib.auth import views, mixins
from .forms import LoginForm, SignUpForm, ProfileUpdateForm, PostUpdateForm, PostDeleteForm, BookCreateForm
from .api.GoogleBooksAPI import get_thumbnail_url
from .recommendations.rating import recommend_user
import numpy as np
import json

class IndexView(generic.ListView):
    template_name = 'shelves/index.html'
    context_object_name = 'posted_list'

    def get_queryset(self):
        return Post.objects.filter(public=True).order_by('-created_at')

class RecommendUserView(generic.ListView):
    template_name = 'shelves/recommend_user.html'
    context_object_name = 'recommend_user_list'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return recommend_user(self.request.user)
        else:
            return []

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

class PostDetailView(generic.DetailView):
    template_name = 'shelves/post_detail.html'
    model = Post

class PostUpdateView(mixins.UserPassesTestMixin, generic.UpdateView):
    raise_exception = False

    model = Post
    form_class = PostUpdateForm
    template_name = 'shelves/post_update.html'

    def test_func(self):
        created_user = Post.objects.get(id=self.kwargs['pk']).created_by.username
        user = self.request.user
        return user.pk == created_user or user.is_superuser

    def get_success_url(self):
        return resolve_url('shelves:post_detail', pk=self.kwargs['pk'])

    def form_valid(self, form):
        form.instance.public = True
        return super().form_valid(form)

class PostDeleteView(mixins.UserPassesTestMixin, generic.DeleteView):
    model = Post
    form_class = PostDeleteForm
    success_url = reverse_lazy('shelves:index')
    template_name = 'shelves/post_delete.html'

    def test_func(self):
        created_user = Post.objects.get(id=self.kwargs['pk']).created_by.username
        user = self.request.user
        return user.pk == created_user or user.is_superuser

class BookSearchView(generic.CreateView):
    model = Book
    template_name = 'shelves/book_search.html'
    form_class = BookCreateForm

    def get_success_url(self):
        return resolve_url('shelves:post_update', pk=self.new_post.pk)

    def form_valid(self, form):
        self.object = form.save()

        self.new_post = Post(item=self.object, created_by=self.request.user, title=self.object.title, rating=2.5)
        self.new_post.save()

        return super().form_valid(form)

    def form_invalid(self, form):
        book = Book.objects.get(pk=form.instance.book_id)

        self.new_post = Post(item=book, created_by=self.request.user, title=book.title, rating=2.5)
        self.new_post.save()

        return HttpResponseRedirect(self.get_success_url())

class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'shelves/book_detail.html'
