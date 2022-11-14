from copy import copy

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView, CreateView, DetailView, ListView


from .forms import CreateStudentForm, StudentFilterForm
from .forms import UpdateStudentForm
from .models import Student


class ListStudentView(ListView):
    model = Student
    template_name = 'students/list.html'

    def get_filter(self):
        students = Student.objects.select_related('group', 'headman_group')
        filter_form = StudentFilterForm(data=self.request.GET, queryset=students)

        return filter_form

    def get_queryset(self):
        students = Student.objects.select_related('group')
        filter_form = StudentFilterForm(data=self.request.GET, queryset=students)

        return filter_form

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_filter().form

        params = self.request.GET
        if 'page' in params:
            params = copy(params)
            del params['page']

        context['params'] = f"&{params.urlencode()}" if params else ''

        return context


class DetailStudentView(LoginRequiredMixin, DetailView):
    model = Student
    template_name = 'students/detail.html'


class CreateStudentView(LoginRequiredMixin, CreateView):
    model = Student
    success_url = reverse_lazy('students:list')
    template_name = 'students/create.html'
    form_class = CreateStudentForm


class UpdateStudentView(LoginRequiredMixin, UpdateView):
    model = Student
    form_class = UpdateStudentForm
    success_url = reverse_lazy('student:list')
    template_name = 'students/update.html'


class DeleteStudentView(LoginRequiredMixin, DeleteView):
    model = Student
    success_url = reverse_lazy('students:list')
    template_name = 'students/delete.html'
