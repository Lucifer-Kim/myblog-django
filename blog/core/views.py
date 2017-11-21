# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse
from core.models import Post


# Create your views here.
def index(request):
    posts = Post.objects.all().order_by('-id')

    return render(request, 'index.html', dict(posts=posts))


def article_detail(request, pk):
    post = Post.objects.get(pk=pk)

    return render(request, 'article_detail.html', dict(post=post))


def hello_world(request):

    return HttpResponse("Hello World!!!")
