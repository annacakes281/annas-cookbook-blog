from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Posted"))


class Post(models.Model):
    recipe_name = models.CharField(max_length=200, unique=False)
    slug = models.SlugField(max_length=200, unique=False)
    written_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="recipe_posts")
    recipe_image = CloudinaryField('image', default='placeholder')
    edited_on = models.DateTimeField(auto_now=True) 
    prep_time = models.CharField(max_length=30)  # poss timefield
    cook_time = models.CharField(max_length=30)  # poss timefield
    ingredients = models.TextField()
    recipe_steps = models.TextField()
    posted_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='recipe_likes', blank=True)

    class Meta:
        ordering = ['-posted_on']  # may change, Django docs

    def __str__(self):
        return self.recipe_name

    def number_of_likes(self):
        return self.likes.count()

# draft need to check in live view to edit comment model fields


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()  # unsure if needed
    body = models.TextField()
    posted_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['posted_on']  # may change, Django docs

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
