from django.db import models
from django.utils import timezone


class DefaultQuerySet(models.QuerySet):
    """
    Prevents objects from being hard-deleted. Instead, sets the
    ``deleted_datetime``, effectively soft-deleting the object.
    """

    def delete(self):
        for obj in self:
            obj.deleted_datetime = timezone.now()
            obj.save()

    def undelete(self):
        for obj in self:
            obj.deleted_datetime = None
            obj.save()


class DefaultManager(models.Manager):
    """
    Only exposes objects that have NOT been soft-deleted.
    """

    def get_queryset(self):
        return DefaultQuerySet(self.model, using=self._db).filter(
            deleted_datetime__isnull=True)
