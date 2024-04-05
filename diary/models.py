from django.db import models

# Create your models here.
class Page(models.Model):
    #title, content, create_date,updated_date
    title = models.CharField(max_length=100)
    content = models.TextField()
    feeling = models.CharField(max_length=80)
    score = models.IntegerField()
    dt_created = models.DateField(verbose_name="Date Created", auto_now_add=True)
    dt_modified = models.DateField(verbose_name="Date Modified", auto_now=True)

    def __str__(self):
        return self.title