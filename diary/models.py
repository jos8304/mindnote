from django.db import models
from .validators import validate_no_hash, validate_no_numbers, validate_score


# Create your models here.
class Page(models.Model):
    #title, content, create_date,updated_date
    title = models.CharField(max_length=10, validators=[validate_no_hash])
    content = models.TextField()
    feeling = models.CharField(max_length=80, validators=[validate_no_hash, validate_no_numbers])
    score = models.IntegerField(validators=[validate_score])
    dt_created = models.DateField(verbose_name="Date Created", auto_now_add=True)
    dt_modified = models.DateField(verbose_name="Date Modified", auto_now=True)

    def __str__(self):
        return self.title