from django.urls import path

from . import views

urlpatterns = [
    path('', views.HelloMask.as_view(), name='mask')
]