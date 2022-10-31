import random

from django.db import models
from faker import Faker

from core.models import PersonModel


class Teacher(PersonModel):
    salary = models.PositiveIntegerField(default=10_000)

    def __str__(self):
        return f'{self.first_name} {self.last_name} (${self.salary})'

    class Meta:
        db_table = 'teachers'

    @classmethod
    def _generate(cls):
        obj = super()._generate()
        obj.salary = random.randint(10_000, 100_000)
        obj.save()

