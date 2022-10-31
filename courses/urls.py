from django.urls import path

from .views import CreateCourseView
from .views import DetailCourseView
from .views import ListCourseView
from .views import UpdateCourseView
from .views import DeleteCourseView

app_name = 'courses'

urlpatterns = [
    path('create/', CreateCourseView.as_view(), name='create'),
    path('', ListCourseView.as_view(), name='list'),
    path('detail/<int:course_id>/', DetailCourseView.as_view(), name='detail'),
    path('update/<int:course_id>/', UpdateCourseView.as_view(), name='update'),
    path('delete/<int:course_id>/', DeleteCourseView.as_view(), name='delete'),
]
