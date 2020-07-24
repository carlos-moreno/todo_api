import uuid

from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from todo.account.models import User


class Todo(models.Model):
    id = models.UUIDField(_("id"), primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(_("name"), max_length=50)
    description = models.TextField(_("description"))
    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    finished_in = models.DateTimeField(_("finished in"), blank=True, null=True)
    done = models.BooleanField(_("done"), default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "todo"
        ordering = ("created_at",)

    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwargs):
        if self.done:
            self.finished_in = timezone.now()
        else:
            self.finished_in = None
        super(Todo, self).save(*args, **kwargs)
