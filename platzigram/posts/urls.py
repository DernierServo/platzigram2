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
        view=views.create_post, 
        name='n_new'
    ),    
]
