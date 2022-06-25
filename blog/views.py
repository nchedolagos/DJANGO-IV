from django.shortcuts import render
from .models import Post
from django.views import generic
# Create your views here.
class PostListView(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'post_list.html'

class PostCreateView(generic.CreateView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    fields = "__all__"
    success_url = reverse_lazy(“blog:all”)

class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

class PostUpdateView(generic.UpdateView):
    model = Post
    template_name = 'post_detail.html'
    fields ='all'
    success_url  = reverse_lazy('blog:all')

class PostDelete(generic.DeleteView):
    model = Post
    template_name = 'post_confirm_delete.html'
    fields = 'all'
    success_url  = reverse_lazy('blog:all')