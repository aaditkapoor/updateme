from django.db import models


class Blogs(models.Model):
    author = models.CharField(max_length=32)
    blog = models.TextField(max_length=300, blank=True, help_text='Enter your blog here-: ')
    date = models.DateTimeField('Date written', auto_created=True)
    approved = models.BooleanField(default=False)
    unique_key = models.SmallIntegerField(auto_created=True)
    likes = models.SmallIntegerField(default=0, editable=True, auto_created=True, help_text='Your likes')
    email = models.EmailField()

    def __unicode__(self):
        return self.author

    def get_likes(self):
        return self.likes

    def increment_like(self):
        self.likes += 1


class Error(models.Model):
    error = models.CharField(max_length=320)
    resolved = models.BooleanField(default=False)
    date = models.DateField('Date reported')

    def __unicode__(self):
        return self.error