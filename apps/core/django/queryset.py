from django.db import models


class BaseQuerySet(models.QuerySet):

    def all(self):
        return super(BaseQuerySet, self).filter()

    def filter(self, *args, **kwargs):
        kwargs.update(dict(is_delete=False))
        return super(BaseQuerySet, self).filter(*args, **kwargs)

    def delete(self):
        self.update(is_delete=True)

    def exclude(self, *args, **kwargs):
        return super(BaseQuerySet, self).exclude(*args, **kwargs).filter(is_delete=False)
