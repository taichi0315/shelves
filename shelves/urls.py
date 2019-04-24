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
    path('post/<int:pk>', views.PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
    path('recommend_user/', views.RecommendUserView.as_view(), name='recommend_user'),
    path('book_search/', views.BookSearchView.as_view(), name='book_search'),
    path('book/<str:pk>', views.BookDetailView.as_view(), name='book_detail'),
]