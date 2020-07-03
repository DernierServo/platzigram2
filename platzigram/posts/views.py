"""Post views."""

# Django
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Forms
from posts.forms import PostForm

# Models
from posts.models import Post





@login_required()
def list_posts(request):
    """List existing posts."""
    posts = Post.objects.all().order_by('-created')
    return render(
        request, 
        'posts/feed.html',
        {
            'posts': posts
        }
    )

@login_required
def create_post(request):
    """Create posts."""
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('posts:n_posts')

    else:
        form = PostForm()

    return render(
        request,
        'posts/new.html',
        {
            'form': form,
            'user': request.user,
            'profile': request.user.profile
        }
    )