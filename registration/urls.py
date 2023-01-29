from django.urls import path
from . import views
urlpatterns = [
    path('',views.register,name='register'),
    path('FIFA/',views.FIFA,name='FIFA'),
]