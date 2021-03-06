from random import choices
from sre_constants import CATEGORY
from unicodedata import category
from django.db import models
from authentication.models import User
# Create your models here.

class Income(models.Model):

    SOURCE_OPTIONS=[
        ('SALARY','SALARY'),
        ('BUSINESS','BUSINESS'),
        ('SITE-HUSTLES','SITE-HUSTLES'),
        ('OTHERS','OTHERS'),
    ]



    source=models.CharField(choices=SOURCE_OPTIONS,max_length=255)
    amount=models.DecimalField(max_digits=10,decimal_places=2,max_length=255)
    description=models.TextField()
    owner=models.ForeignKey(to=User,on_delete=models.CASCADE)
    date=models.DateField(null=False,blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering: ['-updated_at']

    def __str__(self):
        return str(self.owner)+"'s income"