from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=50,)
    duration = models.DurationField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    class Meta:
        db_table = 'courses'
