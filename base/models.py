import uuid
from django.db import models


class SoftDeletionManager(models.Manager):
    def get_queryset(self):
        """
        Return a queryset that filters out any deleted items.

        :param self: The instance of the class.
        :return: A queryset that filters out any deleted items.
        """
        return super().get_queryset().filter(is_deleted=False)

    def all_objects(self):
        """
        Returns all objects in the queryset.

        :param self: The instance of the class.
        :return: The queryset containing all objects.
        """
        return super().get_queryset()


class BaseModel(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)

    objects = SoftDeletionManager()

    all_objects = models.Manager()

    class Meta:
        abstract = True
        ordering = ("-created_at",)
