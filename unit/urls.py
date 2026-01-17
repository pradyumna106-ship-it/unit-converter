from django.urls import path
from . import views

urlpatterns = [
    path('helo/', views.say_hello),
    path("", views.handle_convert, name="handle_convert"),
]