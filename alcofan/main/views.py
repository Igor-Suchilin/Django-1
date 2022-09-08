from http.client import HTTPResponse

from django.shortcuts import render
from .calculations import delta, day_s
from .models import Category, Drinky
day_of_days, days_left = day_s(delta.days)


def index(request):
    cats = Category.objects.all()
    context = {
        'now': delta.days,
        'day': day_of_days,
        'cats': cats,
        'days_left': days_left
    }
    return render(request, 'main/index.html', context=context)


def base(request):
    drinky = Drinky.objects.all()
    context = {
        'drinky': drinky
    }
    return render(request, 'main/base.html', context=context)


def show_post(request, post_id):
    return HTTPResponse(f'Отображение статьи с id = {post_id}')

def show_category(request, cat_id):
    post = Drinky.objects.filter(cat_id=cat_id)
    cat = Category.objects.get(id=cat_id)
    context = {
        'now': delta.days,
        'day': day_of_days,
        'days_left': days_left,
        'post': post,
        'cat': cat,
    }
    return render(request, 'main/base.html', context=context)