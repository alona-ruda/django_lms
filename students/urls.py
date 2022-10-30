from django.urls import path

from .views import CreateStudentView
from .views import DetailStudentView
from .views import ListStudentView
from .views import DeleteStudentView
from .views import UpdateStudentView


app_name = 'students'

urlpatterns = [
    path('create/', CreateStudentView.as_view(), name='create'),                           # Create
    path('', ListStudentView.as_view(), name='list'),
    path('detail/<int:pk>/', DetailStudentView.as_view(), name='detail'),          # Read
    path('update/<int:pk>/', UpdateStudentView.as_view(), name='update'),          # Update
    path('delete/<int:pk>/', DeleteStudentView.as_view(), name='delete'),          # Delete
]
