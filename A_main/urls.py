from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path('', views.index, name="index"),
    path('about_me/', views.about, name="about")
]
