"""Users URLs."""

# Django
from django.urls import path

# Views
from users import views

urlpatterns = [
    # Management
    path(
        route='login/', 
        view=views.login_view, 
        name='n_login'
    ),
    path(
        route='logout/', 
        view=views.logout_view, 
        name='n_logout'
    ),
    path(
        route='signup/', 
        view=views.SignupView.as_view(), 
        name='n_signup'
    ),
    path(
        route='me/profile/', 
        view=views.UpdateProfileView.as_view(), 
        name='n_me-profile'
    ),

    # Posts
    path(
        route='<str:p_username>/',
        view=views.UserDetailView.as_view(),
        name='n_detail'
    ),

]

