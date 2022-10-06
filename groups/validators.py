from datetime import date

from django.core.exceptions import ValidationError


def validate_start_date(value):
    if value <= date.today():
        raise ValidationError("You can't use past time.")
