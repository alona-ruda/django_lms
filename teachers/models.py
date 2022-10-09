from django.core.validators import MinLengthValidator
from django.db import models


class Teacher(models.Model):
    first_name = models.CharField(
        max_length=100,
        verbose_name='first name',
        validators=[MinLengthValidator(2, '"first name" field value less than two symbols')]
    )
    last_name = models.CharField(
        max_length=100,
        verbose_name='last name',
        validators=[MinLengthValidator(2, '"last name" field value less than two symbols')]
    )
    birthday = models.DateField(null=True, blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=13, null=True, blank=True)

    class Meta:
        db_table = 'teachers'
