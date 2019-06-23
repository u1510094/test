from django.db import models
from django.db.models import QuerySet

from core.django.queryset import BaseQuerySet


class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    objects = QuerySet.as_manager()

    class Meta:
        abstract = True


class DeleteModel(models.Model):
    is_delete = models.BooleanField(default=False)

    objects = BaseQuerySet.as_manager()

    class Meta:
        abstract = True

    def delete(self, **kwargs):
        self.is_delete = True
        self.save()
