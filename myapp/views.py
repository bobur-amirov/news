from django.shortcuts import render
from taggit.models import Tag

from .models import News, Category, City


def category_list(request):
    categories = Category.objects.all()

    return {'categories': categories}


def city_list(request):
    cities = City.objects.all()

    return {'cities': cities}


def home(request):
    news = News.objects.all().order_by('-created')

    context = {
        'news': news,
    }

    return render(request, 'home.html', context)


def category_news(request, slug):
    category = Category.objects.get(slug=slug)
    news = News.objects.filter(category=category)

    context = {
        'category': category,
        'news': news,
    }

    return render(request, 'category_news.html', context)


def city_news(request, slug):
    city = City.objects.get(slug=slug)
    news = News.objects.filter(city=city)

    context = {
        'city': city,
        'news': news,
    }

    return render(request, 'city_news.html', context)


def tag_news(request, slug):
    tag = Tag.objects.get(slug=slug)
    news = News.objects.filter(tags=tag).order_by('-created')

    context = {
        'tag': tag,
        'news': news,
    }

    return render(request, 'home.html', context)


def new_detail(request, slug):
    new = News.objects.get(slug=slug)
    news_top = News.objects.all().order_by('-views')[:3]
    news_categories = News.objects.filter(category__news=new)

    new.views += 1
    new.save()

    context = {
        'new': new,
        'news_top':news_top,
        'news_categories': news_categories,
    }

    return render(request, 'new_detail.html', context)