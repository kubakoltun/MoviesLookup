from django.db import models


class Movie(models.Model):
    name='movies'
    title = models.CharField(max_length=255)
    realase_year = models.IntegerField(null=True)
    director = models.CharField(max_length=255, null=True)
    genre = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.title
    
    class Meta:
        app_label ='addsearch'
