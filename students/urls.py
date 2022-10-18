from django.urls import path

from students.views import create_student
from students.views import detail_student
from students.views import get_students
from students.views import update_student
from students.views import delete_student

app_name = 'students'

urlpatterns = [
    path('create/', create_student, name='create'),                           # Create
    path('', get_students, name='list'),
    path('detail/<int:student_id>/', detail_student, name='detail'),          # Read
    path('update/<int:student_id>/', update_student, name='update'),          # Update
    path('delete/<int:student_id>/', delete_student, name='delete'),          # Delete
]
