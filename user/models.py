from django.db import models
from django.contrib.auth.models import User
from quotes.models import Quote
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    quotes = models.ForeignKey(Quote, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.quotes + "written by " + self.user

