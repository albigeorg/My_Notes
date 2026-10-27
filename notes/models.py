from django.db import models

# Create your models here.

class Note(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    CATEGORY_CHOICES = [('personal', 'Personal'),('study', 'Study'),('work', 'Work'),('other', 'Other')]

    category = models.CharField( max_length=20,choices=CATEGORY_CHOICES,default='other')

    def __str__(self):
        return self.title
