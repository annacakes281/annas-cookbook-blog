from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Post

# test home page
# def HomePage(request):
#     return render(request, 'homepage.html')


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-posted_on")
    template_name = 'index.html'
    paginate_by = 5  # edit this when testing with more posts


class ViewRecipe(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.order_by('posted_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "view_recipe.html",
            {
                "post": post,
                "comments": comments,
                "liked": liked
            },
        )
