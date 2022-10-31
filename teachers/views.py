from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView



from .forms import CreateTeacherForm, TeacherFilterForm
from .forms import UpdateTeacherForm
from .models import Teacher


class ListTeacherView(ListView):
    model = Teacher
    template_name = 'teachers/list.html'

    def get_queryset(self):
        teachers = Teacher.objects.all()
        filter_form = TeacherFilterForm(data=self.request.GET, queryset=teachers)

        return filter_form


class DetailTeacherView(LoginRequiredMixin, DetailView):
    model = Teacher
    template_name = 'teachers/detail.html'


class CreateTeacherView(LoginRequiredMixin, CreateView):
    model = Teacher
    success_url = reverse_lazy('teachers:list')
    template_name = 'teachers/create.html'
    form_class = CreateTeacherForm


class UpdateTeacherView(LoginRequiredMixin, UpdateView):
    model = Teacher
    form_class = UpdateTeacherForm
    success_url = reverse_lazy('teachers:list')
    template_name = 'teachers/update.html'


class DeleteTeacherView(DeleteView):
    model = Teacher
    success_url = reverse_lazy('teachers:list')
    template_name = 'teachers/delete.html'

