from django.shortcuts import render
from blog.models import Post, Category

def blog(request):

    posts = Post.objects.all()
    blog_category=Category.objects.all()
    return render(request, 'blog/blog.html', {'blog_category': blog_category, 'posts': posts})