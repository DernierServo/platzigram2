"""Posts URLs."""

# Django
from django.urls import path

# Views
from posts import views

urlpatterns = [
    path(
        route='', 
        view=views.PostsFeedView.as_view(), 
        name='n_posts'
    ),
    path(
        route='posts/new/', 
        view=views.CreatePostView.as_view(), 
        name='n_new'
    ),
    path(
        route='posts/<int:pk>/',
        view=views.PostDetailView.as_view(),
        name='n_detail'
    ),
]
