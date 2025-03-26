from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField('Title', max_length=50, blank=True)
    upload_time = models.DateTimeField(unique = True) # upload_time은 중복되면 안되므로 unique = True
    content = models.TextField('Content')
    
    def __str__(self):
        return self.title