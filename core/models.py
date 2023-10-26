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

    def get_comments(self):
        return self.comments.filter(parent=None).filter(active=True)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, related_name="comments")
    name = models.CharField(max_length=50, null=True)
    parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE)
    body = models.TextField(null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('date_created',)

    def __str__(self):
        return self.body

    def get_comments(self):
        return Comment.objects.filter(parent=self).filter(active=True)

    

    
