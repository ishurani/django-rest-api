from django.db import models

# Create your models here.
class thought(models.Model):
    thought_name = models.CharField(max_length=100)
