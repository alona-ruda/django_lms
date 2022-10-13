from django.urls import path

from teachers.views import create_teacher
from teachers.views import get_teachers
from teachers.views import update_teacher
from teachers.views import detail_teacher
from teachers.views import delete_teacher

app_name = 'teachers'

urlpatterns = [
    path('', get_teachers, name='list'),
    path('create/', create_teacher, name='create'),
    path('update/<int:teacher_id>/', update_teacher, name='detail'),
    path('detail/<int:teacher_id>/', detail_teacher, name='update'),
    path('delete/<int:group_id>/', delete_teacher, name='delete'),
]
