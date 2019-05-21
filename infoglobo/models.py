from django.db import models

class Item(models.Model):
    objects = None
    title = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

    class Meta:
        db_table = 'item'

    def __str__(self):
        return self.title