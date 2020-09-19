from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
     title= models.CharField(max_length=100)
     content= models.TextField()
     date_posted= models.DateTimeField(default=timezone.now)
     author= models.ForeignKey(User,on_delete=models.CASCADE)
     image = models.ImageField(upload_to='images/')
     likes = models.ManyToManyField(User,related_name='likes',blank=True)

     def total_likes(self):
          return self.likes.count()

class Comments(models.Model):
     post=models.ForeignKey(Post,on_delete=models.CASCADE)
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     content=models.TextField()
     timestamp=models.DateTimeField(auto_now_add=True)
     reply= models.ForeignKey('comments',null='True',related_name='replies',on_delete=models.CASCADE)

     def __str__(self):
          return'{}-{}'.format(self.post.title,str(self.user.username))