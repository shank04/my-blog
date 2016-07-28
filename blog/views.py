from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.http import HttpResponse

def post_list(request):
    posts = Post.objects.all
    return render(request, 'blog/post_list.html', {'posts': posts})
    paginate_by=2

def detail(request, try2):
    posts = Post.objects.get(pk=try2)
    #return HttpResponse("<h2>details of blog no." + str(try2) + "</h2>")
    return render(request, 'blog/det.html', {'try2': try2,'posts': posts})

def like(request, try2):
    posts = Post.objects.get(pk=try2)
    if posts.is_liked:
    	posts.is_liked=False
    	posts.save()
    else:
    	posts.is_liked=True
    	posts.save()

    return render(request, 'blog/det.html', {'try2': try2,'posts': posts})

    
    

