from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Client(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Artist(models.Model):
    name = models.CharField(max_length=255)
    works = models.ManyToManyField('Work')


class Work(models.Model):
    LINK_TYPES = [
        ('Y', 'Youtube'),
        ('I', 'Instagram'),
        ('O', 'Other')
    ]
    link = models.URLField()
    type = models.CharField(max_length=1, choices=LINK_TYPES)

@receiver(post_save, sender=User)
def create_client(sender, instance, created, **kwargs):
    if created:
        Client.objects.create(user=instance)