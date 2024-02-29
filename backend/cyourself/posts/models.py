from django.db import models

from personal.models import Storage
from users.models import User


class Post(models.Model):
    title = models.CharField(
        max_length=256,
    )
    text = models.TextField()
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='publication date',
        db_index=True,
    )
    author = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )


class Tag(models.Model):
    title = models.CharField(
        max_length=100
    )
    def __str__(self):
        return f'{self.title}'


class TagPost(models.Model):
    tag = models.ForeignKey(
        Tag,
        on_delete=models.CASCADE
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE
    )
    
    def __str__(self):
        return f'{self.tag.title}'


class Comment(models.Model):
    text = models.TextField()
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='publication date',
        db_index=True,
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )


class Like(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE
    )
    
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user','post'],
                name='one_like_from_one_user'
            )
        ]


class PostStorage(models.Model):
    storage = models.ForeignKey(
        Storage,
        on_delete=models.CASCADE,
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE
    )
    add_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='publication date',
        db_index=True,
    )
    
    class Meta:
        ordering = ('-add_date',)
        constraints = [
            models.UniqueConstraint(
                fields=['storage','post'],
                name='save_post _in_storage_one_time'
            )
        ]
    
