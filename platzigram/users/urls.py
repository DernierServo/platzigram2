"""Posts URLs."""

# Django
from django.urls import path
from django.views.generic import TemplateView
# Views
from users import views

urlpatterns = [
    # Posts
    path(
        route='<str:username>/',
        view=TemplateView.as_view(template_name='users/detail.html'),
        name='n_detail'
    ),

    # Management
    path(
        route='users/login/', 
        view=views.login_view, 
        name='n_login'
    ),
    path(
        route='users/logout/', 
        view=views.logout_view, 
        name='n_logout'
    ),
    path(
        route='users/signup/', 
        view=views.signup, 
        name='n_signup'
    ),
    path(
        route='users/me/profile/', 
        view=views.update_profile, 
        name='n_me-profile'
    ),
]

