from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('recipe/<slug:slug>/', views.ViewRecipe.as_view(), name='view_recipe'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('heart/<slug:slug>', views.PostHeart.as_view(), name='post_heart'),
    path('bookmark/<int:id>', views.add_bookmark, name='add_bookmark'),
    path('contact/', views.contact_page, name='contact'),
    path('my-profile/', views.my_profile, name='profile'),
    path('search-recipes/', views.SearchRecipes.as_view(),name='search_recipes'),
    path('admin/recipe_site/post/add/', views.add_recipe, name='add_recipe'),
    path('admin/recipe_site/comment/', views.manage_comments, name='manage_comments'),
    path('admin/recipe_site/tip/', views.manage_tips, name='manage_tips'),
]
