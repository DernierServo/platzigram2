"""platzigram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views as local_views
from posts import views as posts_views
from users import views as users_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello-world/', local_views.hello_world, name='n_hello_world'),
    path('sorted/', local_views.sorted_numbers, name='n_sorted'),
    path('hi/<str:p_name>/<int:p_age>/', local_views.say_hi, name='n_say_hi'),

    path('posts/', posts_views.list_posts, name='n_posts'),

    path('users/login/', users_views.login_view, name='n_users-login'),
    path('users/logout/', users_views.logout_view, name='n_users-logout'),
    path('users/signup/', users_views.signup, name='n_signup'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
