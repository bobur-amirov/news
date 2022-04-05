from django.urls import path

from .views import home, category_news, city_news, tag_news, new_detail

urlpatterns = [
    path('', home, name='home'),
    path('category/<slug:slug>/', category_news, name='category_news'),
    path('city/<slug:slug>/', city_news, name='city_news'),
    path('tag/<slug:slug>/', tag_news, name='tag_news'),
    path('new/<slug:slug>/', new_detail, name='new_detail'),
]