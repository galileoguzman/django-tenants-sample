from django.urls import path
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    # Django administration site
    path('admin/', admin.site.urls),
    # Static web pages
    path('', TemplateView.as_view(template_name='pages/landing.html'), name='index'),
]
