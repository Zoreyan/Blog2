from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('post_detail/<int:pk>/', post_detail, name='post-detail'),
    path('about_us/', about_us, name='about-us'),
    path('contacts/', contacts, name='contacts'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('sign_up/', sign_up, name='sign-up'),
    path('profile/', post_detail, name='profile'),
    path('new_post/', new_post, name='new-post'),
    path('my_posts/', my_posts, name='my-posts'),

    path('update_post/<int:pk>/', update_post, name='update-post'),
    
    path('post_delete/<int:pk>/', post_delete, name='post-delete'),
]