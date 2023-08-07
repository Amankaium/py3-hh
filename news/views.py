from django.shortcuts import render
from .models import *


def news_detail(request, id):
    new = New.objects.get(id=id)
    new.views_count += 1
    new.user_views.add(request.user)
    new.save()


    new_view_object = NewsViews.objects.get_or_create(
        new=new,
        user=request.user
    )

    return render(request, 'new/new_detail.html', {'new': new})
