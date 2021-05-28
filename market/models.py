from django.db import models

class Product(models.Model):
    title = models.CharField('title', max_length=20, blank=False)
    content = models.TextField('content', max_length=100, blank=False)
    category = models.IntegerField('category', blank=False)
    status = models.IntegerField('status', default=0)
    create_at = models.DateField('create_date', auto_now_add=True)
    update_at = models.DateField('update_date', auto_now=True)

    def __str__(self):
        return self.title