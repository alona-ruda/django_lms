from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView, DetailView, UpdateView, CreateView, ListView

from .forms import CourseCreateForm, CourseUpdateForm
from .models import Course



class ListCourseView(ListView):
    model = Course
    template_name = 'courses/list.html'

class CreateCourseView(LoginRequiredMixin, CreateView):
    model = Course
    success_url = reverse_lazy('courses:list')
    template_name = 'courses/create.html'
    form_class = CourseCreateForm


class UpdateCourseView(LoginRequiredMixin, UpdateView):
    model = Course
    form_class = CourseUpdateForm
    success_url = reverse_lazy('courses:list')
    template_name = 'courses/update.html'




class DetailCourseView(LoginRequiredMixin, DetailView):
    model = Course
    template_name = 'courses/detail.html'


class DeleteCourseView(LoginRequiredMixin, DeleteView):
    model = Course
    success_url = reverse_lazy('courses:list')
    template_name = 'courses/delete.html'

