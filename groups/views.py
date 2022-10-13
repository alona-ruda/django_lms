from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from webargs.fields import Str
from webargs.djangoparser import use_args

from .forms import CreateGroupForm
from .forms import UpdateGroupForm
from .models import Group


@use_args(
    {
        'name_of_group': Str(required=False),
        'start_date': Str(required=False),
    },
    location='query'
)
def get_groups(request, args):
    groups = Group.objects.all()

    if len(args) != 0 and args.get('name_of_group'):
        groups = groups.filter(
            Q(name_of_group=args.get('name_of_group', ''))
        )

    return render(
        request=request,
        template_name='groups/list.html',
        context={
            'title': 'List of groups',
            'groups': groups
        }
    )


def detail_group(request, group_id):
    group = get_object_or_404(pk=group_id)
    return render(request, 'groups/detail.html', {'group': group})


def create_group(request):
    if request.method == 'GET':
        form = CreateGroupForm()
    elif request.method == 'POST':
        form = CreateGroupForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('list'))

    return render(request, 'groups/create.html', {'form': form})


def update_group(request, group_id):
    group = get_object_or_404(pk=group_id)

    if request.method == 'GET':
        form = UpdateGroupForm(instance=group)
    elif request.method == 'POST':
        form = UpdateGroupForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('list'))

    return render(request, 'groups/update.html', {'form': form})


def delete_group(request, group_id):
    group = get_object_or_404(Group, pk=group_id)

    if request.method == 'POST':
        group.delete()
        return HttpResponseRedirect(reverse('list'))

    return render(request, 'groups/delete.html', {'group': group})
