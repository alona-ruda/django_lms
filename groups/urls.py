from django.urls import path

from .views import create_group
from .views import ListGroupView
# from .views import update_group
from .views import detail_group
from .views import delete_group
from .views import UpdateGroupView

app_name = 'groups'

urlpatterns = [
    path('', ListGroupView.as_view(), name='list'),
    path('create/', create_group, name='create'),
    path('update/<int:pk>/', UpdateGroupView.as_view(), name='update'),
    path('detail/<int:group_id>/', detail_group, name='detail'),
    path('delete/<int:group_id>/', delete_group, name='delete'),
]
