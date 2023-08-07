from django.urls import path
from .views import *


urlpatterns = [
    path('<int:id>/', news_detail)
]