from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Post


def post_list(request):
    post = Post.published.all()
    return render(request, 'blog/post/list.html', {'post': post})


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
    return render(request, 'blog/post/detail.html', {'post': post})
