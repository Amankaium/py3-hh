from django.urls import path
from .views import *



urlpatterns = [
    path('list/', recruiter_list, name='recruiter-list'),
    path('list-class/', RecruitView.as_view(), name='recruiter-list-class'),
    path('list-class-generic/', RecruitListView.as_view(), name='recruiter-list-class-generic'),
    path('detail/<int:pk>/', recruiter_detail, name='recruiter-detail'),
    path('create/', RecruiterCreateView.as_view(), name='create-recruiter'),
    path('update/<int:id>/', RecruiterUpdateView.as_view(), name='recruiter-update'),
    path('update-generic/<int:pk>/', RecruiterGenericUpdateView.as_view(), name='recruiter-generic-update'),
]