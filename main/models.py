from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Emails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=100)
    name = models.CharField(max_length=255)
    token = models.CharField(max_length=255)
    host = models.CharField(max_length=255)
    port = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.email} ({self.host}:{self.port})"
    
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    message = models.CharField(max_length=5500)
    subject = models.CharField(max_length=100)
    def __str__(self):
        return self.name 

class Contacts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    email = models.EmailField()
    contacted = models.BooleanField(default=False)
    message = models.ForeignKey(  # <- Nové pole
    'Message',
    on_delete=models.SET_NULL,
    null=True,
    blank=True,
    related_name='contacts'
    )

    def __str__(self):
        return f"{self.name}, {self.company}"
    
