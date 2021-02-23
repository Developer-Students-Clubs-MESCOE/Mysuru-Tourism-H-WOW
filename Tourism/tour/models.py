from django.db import models

# Create your models here.
class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    tel  = models.CharField(max_length=70, default="")
    message = models.CharField(max_length=70, default="")

    def __str__(self):
        return self.name

class Feed(models.Model):
    msg_id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=70, default="")
    message = models.CharField(max_length=70, default="")

    def __str__(self):
        return self.email

class Valo(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    message = models.CharField(max_length=70, default="")

    def __str__(self):
        return self.name

