from django.db import models



# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=225)
    date = models.DateTimeField(auto_now_add=True)

    def __str__ (self):
        return self.title


