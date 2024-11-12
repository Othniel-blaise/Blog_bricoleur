 
from django.urls import path
from . import views
from .views import HomeView,ArticleDetailView,AddPostView
from .views import HomeView,UpdatePostView,DeletePostView,LikeView,instaView
urlpatterns = [
path('', HomeView.as_view(), name='home'),  # L'URL pour la page d'accueil
path('article/<int:pk>',ArticleDetailView.as_view(), name="article-detail"), 
path ('add_post/',AddPostView.as_view(), name ='add_post'),
path('article/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'),
path('article/<int:pk>/remove', DeletePostView.as_view(), name='delete_post'),   
path('like/<int:pk>', LikeView, name='like-post'),   
path ('insta/',views.instaView, name ='instaView'),
 path('post/<int:pk>/like/',views.like_post, name='like-post'),
]
