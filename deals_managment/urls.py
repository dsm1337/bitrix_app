from django.urls import path

from .views import list_deals, add_deal

app_name = 'deals'
urlpatterns = [
    path('', list_deals, name='list'),
    path('add/', add_deal, name='add'),
]