from django.db import models

class Helping(models.Model):
    name = models.CharField(max_length=32,null=True)
    query = models.TextField(max_length=300)
    date = models.DateTimeField('Date submitted: ')
    working = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name
