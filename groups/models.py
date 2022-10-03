from datetime import date

from django.core.validators import MinLengthValidator
from django.db import models # noqa

from groups.validators import validate_start_date


class Group(models.Model):
    name_of_group = models.CharField(
        max_length=50,
        verbose_name="group's name",
        db_column="group's name",
        validators=[MinLengthValidator(2, '"name_of_group" field value less than two symbols')]
    )

    start_date = models.DateField(default=date.today, null=True, blank=True, validators=[validate_start_date])

    group_description = models.TextField()

    class Meta:
        db_table = 'groups'