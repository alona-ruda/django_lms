from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .forms import CourseCreateForm, CourseUpdateForm
from .models import Course


def get_courses(request):
    courses = Course.objects.all()

    return render(request, 'courses/list.html', {'courses': courses})


def create_course(request):
    if request.method == 'POST':
        form = CourseCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('courses:list'))

    form = CourseCreateForm()

    return render(request, 'courses/create.html', {'form': form})



def update_course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    if request.method == 'POST':
        form = CourseUpdateForm(instance=course, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('courses:list'))
    form = CourseUpdateForm(instance=course)
    return render(request, 'courses/update.html', {'form': form, 'course': course})



def detail_course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    return render(request, 'courses/detail.html', {'course': course})


def delete_course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)

    if request.method == 'POST':
        course.delete()
        return HttpResponseRedirect(reverse('list'))

    return render(request, 'courses/delete.html', {'course': course})

