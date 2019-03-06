from django.urls import path, include
from . import views

app_name = 'shelves'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('profile/<str:pk>', views.ProfileView.as_view(), name='profile'),
    path('profile/<str:pk>/update/', views.ProfileUpdateView.as_view(), name='profile_update'),
    path('post/', views.PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>', views.PostDetailView.as_view(), name='post_detail'),
    path('recommend_user/', views.RecommendUserView.as_view(), name='recommend_user'),
]