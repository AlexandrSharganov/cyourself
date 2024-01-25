from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from users.models import User


class Profile(models.Model):
    """Profile model."""

    description = models.CharField(
        verbose_name='description',
        max_length=250,
    )
    author = models.OneToOneField(
        User,
        related_name='profile',
        verbose_name='author',
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'profile'
        verbose_name_plural = 'profiles'

    def __str__(self):
        return f'{self.id}'

@receiver(post_save, sender=User)
def save_or_create_create(sender, instance, created, **kwargs):
    """Создание профайла вместе с пользователем."""
    if created:
        title = f'{instance.username}`s blog'
        Profile.objects.create(author=instance)
