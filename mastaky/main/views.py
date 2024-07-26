from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models


def index(request):
    educations = models.Education.objects.all()
    all_mk = models.MK.objects.all()
    all_student_works = models.StudentWork.objects.all()
    all_reviews = models.Feedback.objects.all()
    context = {
        'educations_item': educations,
        'mk_item': all_mk,
        'all_student_works': all_student_works,
        'all_reviews': all_reviews
    }
    return render(request, 'main.html', context)


def education_detail(request, pk):
    about_education = models.EducationDetail.objects.get(pk=pk)
    context = {
        'about': about_education
    }
    return render(request, 'education_detail.html', context)


def mk_detail(request, pk):
    about_mk = models.MkDetail.objects.get(pk=pk)
    context = {
        'about_mk': about_mk
    }
    return render(request, 'mk_detail.html', context)


def join_up_form_view(request):
    if request.method == 'POST':
        return redirect('join_up_success')

    return render(request, 'join_up_form.html')


def join_up_success_view(request):
    return render(request, 'join_up_success.html')


# Create your views here.
