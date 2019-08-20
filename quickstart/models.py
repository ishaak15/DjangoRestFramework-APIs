from django.db import models

# Create your models here.


class DataSet(models.Model):
    data = models.CharField(max_length=20,blank=False)

    def __str__(self):
        return self.data
