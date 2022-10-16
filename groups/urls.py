from django.urls import path

from groups.views import create_group
from groups.views import get_groups
from groups.views import update_group
from groups.views import detail_group
from groups.views import delete_group

app_name = 'groups'

urlpatterns = [
    path('', get_groups, name='list'),
    path('create/', create_group, name='create'),
    path('update/<int:group_id>/', update_group, name='update'),
    path('detail/<int:group_id>/', detail_group, name='detail'),
    path('delete/<int:group_id>/', delete_group, name='delete'),
]
