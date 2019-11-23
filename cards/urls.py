from django.urls import path
from . import views

urlpatterns = [
    path('', views.List.as_view())
]