from django.shortcuts import render
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    ListView,
    DeleteView
)


# Create your views here.

from .models import Post

class PostListView(ListView):
    template_name = 'blog/blog.html'
    queryset = Post.objects.all()

class BlogDetailView(DetailView):
    template_name = 'blog/post.html'
    queryset = Post.objects.all()



