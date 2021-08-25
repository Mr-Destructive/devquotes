from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

STATUS = (
        (0,"Publish"),
        (1,"Draft"),
        )

class Quote(models.Model):
    quote = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='quotee')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, related_name='quote_likes', null=True)

    def total_likes(self):
        return self.likes.count()

    class Meta:
        ordering = ['-created']

    def get_absolute_url(self):  
        return reverse('quote', args=(str(self.id),))

    def __str__(self):
        return self.quote



