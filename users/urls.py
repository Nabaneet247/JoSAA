# users/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.UserFormView.as_view(), name='signup'),
]