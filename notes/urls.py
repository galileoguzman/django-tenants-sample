from django.urls import path

from .views import index

urlpatterns = [
    # Static web pages
    path('', index, name='index'),
]
