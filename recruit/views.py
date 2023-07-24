from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Recruiter


def recruiter_list(request):
    recruiters = Recruiter.objects.all()
    return render(request, 'recruit/list.html', {'recruiters': recruiters})


def recruiter_detail(request, pk):
    recruiter_object = Recruiter.objects.get(pk=pk)
    return render(
        request,
        'recruit/detail.html',
        {'recruiter_object': recruiter_object}
    )

class RecruitView(View):
    def get(self, request):
        recruiters = Recruiter.objects.all()
        return render(request, 'recruit/list.html', {'recruiters': recruiters})


class RecruitListView(LoginRequiredMixin, ListView):
    model = Recruiter


class RecruiterCreateView(CreateView):
    model = Recruiter
    fields = '__all__'
