from django.db import models
from django.urls import reverse



# Create your models here.

class bloglar(models.Model):
    title = models.CharField(max_length=100, verbose_name='Basliq')
    text = models.TextField(verbose_name='metn')
    viewcount = models.IntegerField(verbose_name='baxis sayi',default=1)
    createddate = models.DateTimeField(auto_now_add=True, verbose_name='yaradilma tarixi')

    def blogdetail(self):
        return reverse('detail', kwargs={'id': self.id})

