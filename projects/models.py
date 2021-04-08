import uuid

from django.db import models
from django.conf import settings
from django.utils import timezone
from django.dispatch import receiver
from django.utils.text import slugify
from django.db.models.signals import pre_save


class Project(models.Model):
    developer = models.ManyToManyField(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=25)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    slug = models.SlugField(max_length=50, unique=True)
    state = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=timezone.now)
    updated_at = models.DateTimeField(auto_now=timezone.now)


@receiver(pre_save, sender=Project)
def set_slug_project(sender, instance, *args, **kwargs):
    if instance.title and not instance.slug:
        slug = slugify(instance.title)
        while Project.objects.filter(slug=slug).exists():
            slug = slugify(
                f'{instance.title}-{str(uuid.uuid4())[:8]}'
            )

        instance.slug = slug
