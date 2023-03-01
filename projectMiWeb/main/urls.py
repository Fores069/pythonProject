from . import views
from django.urls import path

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('posts/', views.posts_page, name='posts_page'),
    path('interested/', views.interested_page, name='interested_page'),
    path('following/', views.following_page, name='following_page'),
    path('post/<int:post_id>/', views.show_post, name='post'),
    path('category/<int:cat_id>/', views.show_category, name='category'),
]