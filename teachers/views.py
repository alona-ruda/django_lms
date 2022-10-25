
from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView

from webargs.fields import Str
from webargs.djangoparser import use_args

from .forms import CreateTeacherForm
from .forms import UpdateTeacherForm
from .models import Teacher


@use_args(
    {
        'first_name': Str(required=False),
        'last_name': Str(required=False),
    },
    location='query'
)
def get_teachers(request, args):
    teachers = Teacher.objects.all()

    if len(args) != 0 and args.get('first_name') or args.get('last_name'):
        teachers = teachers.filter(
            Q(first_name=args.get('first_name', '')) | Q(last_name=args.get('last_name', ''))
        )

    return render(
        request=request,
        template_name='teachers/list.html',
        context={
            'title': 'List of teachers',
            'teachers': teachers
        }
    )


class DetailTeacherView(DetailView):
    model = Teacher
    template_name = 'teachers/detail.html'


class CreateTeacherView(CreateView):
    model = Teacher
    success_url = reverse_lazy('teachers:list')
    template_name = 'teachers/create.html'
    form_class = CreateTeacherForm


class UpdateTeacherView(UpdateView):
    model = Teacher
    form_class = UpdateTeacherForm
    success_url = reverse_lazy('teachers:list')
    template_name = 'teachers/update.html'


class DeleteTeacherView(DeleteView):
    model = Teacher
    success_url = reverse_lazy('teachers:list')
    template_name = 'teachers/delete.html'

