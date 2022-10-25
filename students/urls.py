from django.urls import path

from .views import create_student
from .views import detail_student
from .views import get_students
# from .views import update_student
from .views import delete_student
# from .views import CustomUpdateStudentView
from .views import UpdateStudentView


app_name = 'students'

urlpatterns = [
    path('create/', create_student, name='create'),                           # Create
    path('', get_students, name='list'),
    path('detail/<int:student_id>/', detail_student, name='detail'),          # Read
    path('update/<int:pk>/', UpdateStudentView.as_view(), name='update'),          # Update
    # path('update/<int:pk>/', CustomUpdateStudentView.update, name='update'),  # Update
    # path('update/<int:student_id>/', update_student, name='update'),          # Update
    path('delete/<int:student_id>/', delete_student, name='delete'),          # Delete
]
