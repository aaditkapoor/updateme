from django.db import models

class Contact(models.Model):
    email = models.EmailField()
    phone_number = models.BigIntegerField()
    message = models.TextField(max_length=300)
    date = models.DateTimeField('Date given: ')
    notified = models.BooleanField(default=False)
    email_sent = models.BooleanField(default=False)
    uploaded_file = models.FileField(upload_to='/upload/')


    def __unicode__(self):
        return self.phone_number



