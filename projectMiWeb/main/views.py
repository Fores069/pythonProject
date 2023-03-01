from django.http import Http404
from django.shortcuts import render,HttpResponse
from .models import Posts, Category


def home_page(request):
    return render(request,'main/index.html')


def posts_page(request):
    posts = Posts.objects.all()
    return render(request,'main/posts_page.html', {'posts': posts})


def interested_page(request):
    return render(request,'main/interested.html', {'cat_selected':0})


def following_page(request):
    return render(request,'main/following_page.html')


def show_post(request, post_id):
    post = Posts.objects.get(id=post_id)
    return render(request,'main/post_detail.html',{'post_id': post_id,'post': post})


def show_category(request, cat_id):
    posts = Posts.objects.filter(cat_id=cat_id)
    cat_name = Category.objects.get(id=cat_id)
    if len(posts) == 0:
        raise Http404()
    return render(request,'main/category_detail.html',{'cat_id': cat_id, 'posts': posts, 'cat_selected':cat_id, 'cat_name':cat_name})