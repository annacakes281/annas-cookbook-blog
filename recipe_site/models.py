from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Posted"))
CATEGORY = ((0, "Drinks"), (1, "AirFryer"))


class Post(models.Model):
    # main recipe post model for the blog
    recipe_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    written_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="recipe_posts")
    recipe_image = CloudinaryField('image', default='placeholder')
    edited_on = models.DateTimeField(auto_now=True)
    excerpt = models.TextField(blank=True)
    prep_time = models.CharField(max_length=30)
    cook_time = models.CharField(max_length=30)
    ingredients = models.TextField()
    recipe_steps = models.TextField()
    posted_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='recipe_likes', blank=True)
    hearts = models.ManyToManyField(
        User, related_name='recipe_hearts', blank=True)
    bookmarks = models.ManyToManyField(
        User, related_name='bookmark', blank=True)

    class Meta:
        ordering = ['-posted_on']

    def __str__(self):
        return self.recipe_name

    def number_of_likes(self):
        return self.likes.count()

    def number_of_hearts(self):
        return self.hearts.count()


class Comment(models.Model):
    # comment model for the blog
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    comment = models.TextField()
    posted_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['posted_on']

    def __str__(self):
        return f"Comment {self.comment} by {self.name}"


class Tip(models.Model):
    # tips and recommendation model for the blog
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="tips")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    tip = models.TextField()
    posted_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['posted_on']

    def __str__(self):
        return f"Tip {self.tip} by {self.name}"


class Drink(models.Model):
    # drinks model for the blog
    drink_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    written_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="drink_posts")
    drinks_image = CloudinaryField('image', default='placeholder')
    edited_on = models.DateTimeField(auto_now=True)
    excerpt = models.TextField(blank=True)
    prep_time = models.CharField(max_length=30)
    ingredients = models.TextField()
    drink_steps = models.TextField()
    posted_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    category = models.IntegerField(choices=CATEGORY, default=0)
    likes = models.ManyToManyField(
        User, related_name='drink_likes', blank=True)
    hearts = models.ManyToManyField(
        User, related_name='drink_hearts', blank=True)
    bookmarks = models.ManyToManyField(
        User, related_name='drink_bookmark', blank=True)

    class Meta:
        ordering = ['-posted_on']

    def __str__(self):
        return self.drink_name

    def number_of_likes(self):
        return self.likes.count()

    def number_of_hearts(self):
        return self.hearts.count()
