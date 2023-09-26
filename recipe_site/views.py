from django.shortcuts import render
from django.views import generic
from .models import Post


# def HomePage(request):
#     return render(request, 'homepage.html')

class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-posted_on")
    template_name = 'index.html'
    paginate_by = 5
