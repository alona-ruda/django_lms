from datetime import datetime

from django.db import models
from faker import Faker

from core.models import BaseModel
from groups.validators import validate_start_date
from teachers.models import Teacher


class Group(BaseModel):
    name = models.CharField(
        max_length=50,
    )
    start_date = models.DateField(default=datetime.utcnow, validators=[validate_start_date])
    end_date = models.DateField(null=True, blank=True,)
    headman = models.OneToOneField(
        'students.Student',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='headman_group'
    )
    course =models.OneToOneField(
        'courses.Course',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='course'
    )
    teachers = models.ManyToManyField(
        to=Teacher,
        null=True,
        blank=True,
        related_name='groups'
    )


    class Meta:
        db_table = 'groups'

    def __str__(self):
        return f'Group name: <{self.name}>'

    @classmethod
    def gen_group(cls):
        f = Faker()
        lst = [
            'Python',
            'Java',
            'PM',
            'DevOps',
            'Frontend',
            'QA'
        ]

        for group in lst:
            Group.objects.create(
                name=group
            )