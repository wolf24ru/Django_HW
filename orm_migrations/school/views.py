from django.views.generic import ListView
from django.shortcuts import render

from .models import Student


def students_list(request):
    template = 'school/students_list.html'
    students = Student.objects.prefetch_related('teacher').order_by('group', 'name')
    context = {
        'students': students,
               }

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by

    return render(request, template, context)
