from random import choice

from django.db import models

from core.models import PersonModel
from groups.models import Group


class Student(PersonModel):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True, related_name='students')


    def __str__(self):
        if self.group is None:
            return f'{self.first_name} {self.last_name}'
        else:
            return f'{self.first_name} {self.last_name} ({self.group.name})'



    class Meta:
        db_table = 'students'

    @classmethod
    def _generate(cls):
        obj = super()._generate()
        groups = Group.objects.all()
        obj.group = choice(groups)
        obj.save()
