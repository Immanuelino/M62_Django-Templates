# django_templates/urls.py
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home'),  # Home view
    path('filtros/', views.filtered_view, name='filtros'),
    path('ciclo/', views.for_loop_view, name='ciclo'),
]
