from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Post, PostMask

# Create your views here.
class HelloMask(TemplateView):
    template_name = 'home.html'

class PostListView(ListView):
    model = Post
    template_name = 'mask.html'

class PostDetailView(DetailView):
    model = PostMask
    template_name = 'mask_detail.html'