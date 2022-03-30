from django.shortcuts import render,get_object_or_404
from .models import post

def render_posts(request):
    posts = post.objects.all()
    return render(request,'post.html',{'posts':posts})

def post_detail(request, post_id):
    Post = get_object_or_404(post,pk=post_id)
    return render(request,'post_details.html',{"post":Post})

