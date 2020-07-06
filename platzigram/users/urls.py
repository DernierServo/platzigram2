"""Posts URLs."""

# Django
from django.urls import path

# Views
from users import views

urlpatterns = [
    # Posts
    path(
        route='<str:p_username>/',
        view=views.UserDetailView.as_view(),
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

