from django.shortcuts import render
from django.http import Http404
from .models import Post


def post_list(request):
    post = Post.published.all()
    return render(request, 'blog/post/list.html', {'post': post})


def post_detail(request, post_id):
    try:
        post = Post.published.get(id=post_id)
    except Post.DoesNotExist:
        raise Http404('No Post Found')

    return render(request, 'blog/post/detail.html', {'post': post})
