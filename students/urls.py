from django.urls import path

from .views import CreateStudentView
from .views import DetailStudentView
from .views import get_students
# from .views import update_student
from .views import DeleteStudentView
# from .views import CustomUpdateStudentView
from .views import UpdateStudentView


app_name = 'students'

urlpatterns = [
    path('create/', CreateStudentView.as_view(), name='create'),                           # Create
    path('', get_students, name='list'),
    path('detail/<int:pk>/', DetailStudentView.as_view(), name='detail'),          # Read
    path('update/<int:pk>/', UpdateStudentView.as_view(), name='update'),          # Update
    # path('update/<int:pk>/', CustomUpdateStudentView.update, name='update'),  # Update
    # path('update/<int:student_id>/', update_student, name='update'),          # Update
    path('delete/<int:pk>/', DeleteStudentView.as_view(), name='delete'),          # Delete
]
