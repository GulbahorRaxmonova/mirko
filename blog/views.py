from django.shortcuts import render
from django.urls import reverse_lazy

from  django.views.generic import ListView,DetailView, CreateView,UpdateView,DeleteView
from .models import Post


# Create your views here.
class HomePageVieew(ListView):
    model = Post
    template_name = 'base.html'

class ArticlePageVieew(ListView):
    model = Post
    template_name = 'article.html'

class TermsPageVieew(DetailView):
    model = Post
    template_name = 'terms.html'


class PrivacyPageVieew(DetailView):
    model = Post
    template_name = 'privacy.html'




class DetailPageView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class CreatePostView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'body', 'author']

class UpdatePostView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']
class DeletePostView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url=reverse_lazy('home')

