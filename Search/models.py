from django.db import models

class SiteSection(models.Model):
    section1 = models.CharField(max_length=32,default='help')
    section2 = models.CharField(max_length=32,default='blogs')
    section3 = models.CharField(max_length=32,default='contact')
    models.CharField()

