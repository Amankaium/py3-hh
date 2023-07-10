from django.contrib import admin
from .models import Vacancy, Category, Company


admin.site.register(Vacancy)
admin.site.register(Category)
admin.site.register(Company)