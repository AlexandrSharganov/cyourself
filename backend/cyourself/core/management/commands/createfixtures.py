from django.core.management.base import BaseCommand, CommandError

from mixer.backend.django import mixer

from posts.models import TagPost


class Command(BaseCommand):
    "Make fixtures without any arguments."

    def handle(self, *args, **options):
        users = mixer.cycle(10).blend('users.user')
        superuser = mixer.blend(
            'users.user',
            email='admin@admin.admin',
            is_superuser=True,
            is_staff=True
        )
        superuser.set_password('admin')
        superuser.save()
        tags = mixer.cycle(100).blend('posts.tag')
        posts = mixer.cycle(100).blend('posts.post', author=mixer.SELECT)
        for post in posts:
            mixer.blend('posts.tagpost', tag=mixer.SELECT, post=post)
            mixer.blend('posts.like', user=mixer.SELECT, post=post)
        mixer.cycle(200).blend('posts.comment', author=mixer.SELECT, post=mixer.SELECT)
