from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from django.utils import timezone
from .models import Post

def post_detail(request, pk):
    # Post.objects.get(pk=pk)
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


 # smaple
class SampleAppList(ListView):
    template_name = 'blog/post_list0.html'
    model = Post
