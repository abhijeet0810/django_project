from django.urls import path, include

from .views import PostListView

from . import views

urlpatterns = [
            # ex: http://127.0.0.1:8000/blog/ (the blog page)
            path('', PostListView.as_view(), name = 'blog-list'),
            #
            path('<int:pk>', DetailView.as_view(model=Post, template_name='blog/post.html')),
]

'''
urlpatterns = [
    # ex: /personal/
    path('', ListView.as_view(queryset=Post.objects.all().order_by("-date")[:25], template_name="blog/blog.html")),, name='index'),

]

'''

'''
path(ListView.as_view(queryset=Post.objects.all().order_by("-date")[:25],template_name="blog/blog.html")),
                path(ListView.as_view(queryset=Post.objects.all().order_by("-date")[:25], template_name="blog/blog.html")), name='blog-list'),

'''