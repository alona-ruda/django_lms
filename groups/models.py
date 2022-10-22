from datetime import datetime

from django.core.validators import MinLengthValidator
from django.db import models

from groups.validators import validate_start_date


class Group(models.Model):
    name = models.CharField(
        max_length=50,
    )
    start_date = models.DateField(default=datetime.utcnow, validators=[validate_start_date])
    end_date = models.DateField(null=True, blank=True,)
    create_datetime = models.DateTimeField(auto_now_add=True)
    update_datetime = models.DateTimeField(auto_now=True)
    group_description = models.TextField()

    class Meta:
        db_table = 'groups'

    def __str__(self):
        return f'Group name: <{self.name}>'
