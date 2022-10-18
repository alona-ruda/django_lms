from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse


from .forms import GroupUpdateForm
from .forms import GroupCreateForm

from .models import Group


def get_groups(request):
    groups = Group.objects.all()

    return render(request, 'groups/list.html', {'groups': groups})


def detail_group(request, group_id):
    group = get_object_or_404(Group, pk=group_id)
    return render(request, 'groups/detail.html', {'group': group})


def create_group(request):
    if request.method == 'GET':
        form = GroupCreateForm()
    elif request.method == 'POST':
        form = GroupCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('list'))

    return render(request, 'groups/create.html', {'form': form})


def update_group(request, group_id):
    group = get_object_or_404(Group, pk=group_id)
    if request.method == 'POST':
        form = GroupUpdateForm(instance=group, data=request.GET)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('groups:list'))
    form = GroupUpdateForm(instance=group)
    return render(request, 'groups/update.html', {'form': form, 'group': group})


def delete_group(request, group_id):
    group = get_object_or_404(Group, pk=group_id)

    if request.method == 'POST':
        group.delete()
        return HttpResponseRedirect(reverse('list'))

    return render(request, 'groups/delete.html', {'group': group})
