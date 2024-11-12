from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse	
from datetime import datetime,date
class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255, blank=True, null=True)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post_date = models.DateField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='liked_posts', blank=True)

     # Ajout des champs pour image et légende
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    caption = models.TextField(blank=True, null=True)

    def total_likes(self):
        return self.likes.count()
def __str__(self):
		return self.title + ' | ' + str(self.author)

def get_absolute_url(self):
	return reverse('home')





