from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponseRedirect
from django.views import generic, View
from .models import Post, ContactMe
from .forms import CommentForm, TipForm, ContactMeForm


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-posted_on")
    template_name = 'index.html'
    paginate_by = 6  # edit this when adding different sections


class ViewRecipe(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.order_by('posted_on')
        tips = post.tips.order_by('posted_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "view_recipe.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,  # change to false if have approval
                "tips": tips,
                "tipped": True,
                "liked": liked,
                "comment_form": CommentForm(),
                "tip_form": TipForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.order_by('posted_on')
        tips = post.tips.order_by('posted_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        tip_form = TipForm(data=request.POST)
        if tip_form.is_valid():
            tip_form.instance.email = request.user.email
            tip_form.instance.name = request.user.username
            tip = tip_form.save(commit=False)
            tip.post = post
            tip.save()
        else:
            tip_form = TipForm()

        return render(
            request,
            "view_recipe.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "tips": tips,
                "tipped": True,
                "liked": liked,
                "comment_form": CommentForm(),
                "tip_form": TipForm()
            },
        )


class PostLike(View):

    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('view_recipe', args=[slug]))


class ContactPage(generic.ListView):
    model = ContactMe
    template_name = 'contact_form.html'


# class ContactView(View):
    # still need to add this, just want it functional that it sends off but onto admin panel
    # can use similar method to the comment tips
