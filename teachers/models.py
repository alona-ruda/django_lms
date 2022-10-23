import random

from django.core.validators import MinLengthValidator
from django.db import models
from faker import Faker

from students.models import VALID_DOMAIN_LIST


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

    @classmethod
    def generate_fake_data(cls, cnt):
        f = Faker()

        for _ in range(cnt):
            first_name = f.first_name()
            last_name = f.last_name()
            email = f'{first_name}.{last_name}{f.random.choice(VALID_DOMAIN_LIST)}'
            birthday = f.date()
            phone = random.randint(380500000000, 380509999999)
            st = cls(first_name=first_name, last_name=last_name, birthday=birthday, email=email, phone=phone)
            try:
                st.full_clean()
                st.save()
            except:
                print('Incorrect data')

