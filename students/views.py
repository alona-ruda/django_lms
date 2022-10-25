from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import UpdateView, DeleteView, CreateView, DetailView

# from core.views import CustomUpdateBaseView
from .forms import CreateStudentForm, StudentFilterForm
from .forms import UpdateStudentForm
from .models import Student



def get_students(request):
    students = Student.objects.select_related('group')

    filter_form = StudentFilterForm(data=request.GET, queryset=students)

    return render(
        request=request,
        template_name='students/list.html',
        context={'filter_form': filter_form}
    )


class DetailStudentView(DetailView):
    model = Student
    template_name = 'students/detail.html'


class CreateStudentView(CreateView):
    model = Student
    success_url = reverse_lazy('students:list')
    template_name = 'students/create.html'
    form_class = CreateStudentForm

# class CustomUpdateStudentView(CustomUpdateBaseView):
#     model = Student
#     form_class = UpdateStudentForm
#     success_url = 'student:list'
#     template_name = 'students/update.html'

class UpdateStudentView(UpdateView):
    model = Student
    form_class = UpdateStudentForm
    success_url = reverse_lazy('student:list')
    template_name = 'students/update.html'


class DeleteStudentView(DeleteView):
    model = Student
    success_url = reverse_lazy('students:list')
    template_name = 'students/delete.html'


