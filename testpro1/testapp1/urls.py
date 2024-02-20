from django.urls import path
from .views import create_view, details, fetch_data

urlpatterns = [
    path('demo/', create_view),
    path('demo/<int:pk>/', details),
    path('demo1/', fetch_data),
]
