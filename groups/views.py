from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import UpdateView, ListView, DeleteView, DetailView

from students.models import Student
from .forms import GroupUpdateForm
from .forms import GroupCreateForm

from .models import Group


# def get_groups(request):
#     groups = Group.objects.all()
#
#     return render(request, 'groups/list.html', {'groups': groups})

class ListGroupView(ListView):
    model = Group
    template_name = 'groups/list.html'


def detail_group(request, group_id):
    group = get_object_or_404(Group, pk=group_id)
    return render(request, 'groups/detail.html', {'group': group})


def create_group(request):
    if request.method == 'POST':
        form = GroupCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('groups:list'))

    form = GroupCreateForm()

    return render(request, 'groups/create.html', {'form': form})


# def update_group(request, group_id):
#     group = get_object_or_404(Group, pk=group_id)
#     if request.method == 'POST':
#         form = GroupUpdateForm(instance=group, data=request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('groups:list'))
#     form = GroupUpdateForm(instance=group)
#
#     return render(
#         request,
#         'groups/update.html',
#         {
#             'form': form,
#             'group': group,
#             'students': group.students.prefetch_related('headman_group')
#         })

class UpdateGroupView(UpdateView):
    model = Group
    form_class = GroupUpdateForm
    success_url = reverse_lazy('groups:list')
    template_name = 'groups/update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['students'] = self.get_object().students.prefetch_related('headman_group')

        return context

    def get_initial(self):
        initial = super().get_initial()
        try:
            initial['headman_field'] = self.object.headman.pk
        except AttributeError:
            initial['headman_field'] = 0

        return initial

    def form_valid(self, form):
        response = super().form_valid(form)
        pk = int(form.cleaned_data['headman_field'])
        if pk:
            form.instance.headman = Student.objects.get(pk=pk)
        else:
            form.instance.headman = None
        form.save()

        return response

def delete_group(request, group_id):
    group = get_object_or_404(Group, pk=group_id)

    if request.method == 'POST':
        group.delete()
        return HttpResponseRedirect(reverse('list'))

    return render(request, 'groups/delete.html', {'group': group})
