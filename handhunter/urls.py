"""
URL configuration for handhunter project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from core.views import *
from worker.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name='home'),
    path('about/', about),
    path('contacts/', contact_view),
    path('address/', address),
    path('vacancies/', vacancy_list),
    path('vacancy/<int:id>/', vacancy_detail, name='vacancy-info'),
    path('vacancy-edit/<int:id>/', vacancy_edit, name='vacancy-edit'),
    path('add-vacancy/', vacancy_add),
    path('add-vacancy-df/', vacancy_add_via_django_form),
    path("workers/", workers),
    path("worker/<int:id>/", worker_info),
    path("resume-list/", resume_list),
    path("resume-info/<int:id>/", resume_info),
    path("resume-edit/<int:id>/", resume_edit, name="resume-edit"),
    path('add-resume/', add_resume, name='add-resume'),
    path("my-resume/", my_resume, name='my-resume'),
    path('search/', search, name='search'),
    path('registration/', reg_view, name='reg'),
    path('sign-in/', sign_in, name='sign-in'),
    path('login-generic/', LoginView.as_view(), name='login-generic'),
    path('sign-out/', sign_out, name='sign-out'),
    path('create-company/', create_company, name='create-company'),
    path('company-edit/<int:id>/', company_update, name='edit-company'),
    path('recruit/', include('recruit.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# ...:8000/static/my_style.css  #  .../handhunter/core/static/my_style.css

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

