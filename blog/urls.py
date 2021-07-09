from django.urls import path
from .views import (
	PostListView, 
	PostDetailView, 
	PostCreateView,
	PostUpdateView,
	PostDeleteView,
    UserProfileView,
    UserPostView
    )
from . import views

urlpatterns = [
    path('job/', PostListView.as_view(), name='blog-job'),
    path('job/<str:username>', UserProfileView.as_view(), name='user-profile'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/create_job/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('', views.index, name='welcome'),
    path('home/', views.homepage, name='blog-homepage'),
    path('dashboard/', views.dashboard, name='blog-dashboard'),
    path('company/', views.company, name='company'),
    path('myproject/', UserPostView.as_view(), name='blog-mypost'),
    path('profile/<str:username>', views.get_user_profile, name='profile-user'),
    path('admin/', views.admin, name='admin'),

    
]