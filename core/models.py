from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

    

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    question = models.TextField(null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='liked_posts')
    
    
    class Meta:
        ordering = ['-date_added']
        
        
    def __str__(self):
        return self.question
    
    def num_of_likes(self):
        return self.likes.count()
    
    def get_absolute_url(self):
        return reverse("core:detail", kwargs={"pk": self.pk})

    

    
