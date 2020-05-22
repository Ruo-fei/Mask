from django.urls import path

from . import views

urlpatterns = [
    path('home/', views.HelloMask.as_view(), name='home'),
    path('mask/', views.PostListView.as_view(), name='mask'),
    path('mask/<int:pk>/', views.PostDetailView.as_view(), name='mask_detail'),
]