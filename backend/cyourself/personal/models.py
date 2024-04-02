from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Q, F

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


class Storage(models.Model):
    user = models.OneToOneField(
        User,
        related_name='storage',
        verbose_name='user',
        on_delete=models.CASCADE
    )


class Follow(models.Model):
    follower = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='subscriber'
    )
    following = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='following'
    )
    
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['follower','following'],
                name='one_time_follow'
            ),
            models.CheckConstraint(
                check=~Q(follower=F('following')),
                name='no_self_subscription'
            )
        ]
    

@receiver(post_save, sender=User)
def save_or_create(sender, instance, created, **kwargs):
    """Создание профайла вместе с пользователем."""
    if created:
        # title = f'{instance.username}`s blog'
        Profile.objects.create(author=instance)
        Storage.objects.create(user=instance)
