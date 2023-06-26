from django.shortcuts import render
from .models import Worker


def workers(request):
    workers_queryset = Worker.objects.all()
    return render(request, "workers.html", {'workers': workers_queryset})

def worker_info(request, id):
    worker_object = Worker.objects.get(id=id)
    # SELECT * FROM Worket WHERE id={id}
    vacancies = worker_object.vacancy_set.all()
    context = {
        "worker": worker_object,
        "vacancies": vacancies,
    }
    return render(request, "worker.html", context)
