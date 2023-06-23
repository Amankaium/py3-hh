from django.shortcuts import render
from .models import Worker


def workers(request):
    workers_queryset = Worker.objects.all()
    return render(request, "workers.html", {'workers': workers_queryset})
