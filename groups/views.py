from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import UpdateView, ListView, DeleteView, DetailView, CreateView

from students.models import Student
from .forms import GroupUpdateForm
from .forms import GroupCreateForm

from .models import Group


class ListGroupView(ListView):
    model = Group
    template_name = 'groups/list.html'


class DetailGroupView(DetailView):
    model = Group
    template_name = 'groups/detail.html'


class CreateGroupView(CreateView):
    model = Group
    success_url = reverse_lazy('groups:list')
    template_name = 'groups/create.html'
    form_class = GroupCreateForm


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


class DeleteGroupView(DeleteView):
    model = Group
    success_url = reverse_lazy('groups:list')
    template_name = 'groups/delete.html'
