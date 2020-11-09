from django.db import models
class Post(models.Model):
 Nama = models.CharField(max_length=120, help_text='title of message.')
 Asal = models.TextField(help_text="what's on your mind ...")
 pesan = models.CharField(max_length=1000, default='APA AJA')
 def __str__(self):
  return self.Nama