from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Post

# Create your views here.
class SampleAppList(ListView):
    template_name = 'blog/post_list.html'
    model = Post


def post_list(request):
    return render(request, 'blog/post_list.html', {})
