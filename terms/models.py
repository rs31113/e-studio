from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


class Offer(models.Model):
    name = models.CharField(max_length=100, default="public offer")
    text = CKEditor5Field(config_name="default")

    def __str__(self):
        return self.name


__all__ = ()
