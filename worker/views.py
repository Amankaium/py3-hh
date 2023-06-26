from django.shortcuts import render
from .models import Worker, Resume


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


def resume_list(request):
    resume_query = Resume.objects.all()
    return render(
        request, 'resume/resume_list.html',
        {"resumes": resume_query}
    )


def resume_info(request, id):
    resume_object = Resume.objects.get(id=id)
    return render(
        request, 'resume/resume_detail.html',
        {'resume': resume_object}
    )


def my_resume(request):
    resume_query = Resume.objects.filter(worker=request.user.worker)
    # resume_query = request.user.worker.resume.all()
    return render(
        request, 'resume/resume_list.html',
        {"resumes": resume_query}
    )