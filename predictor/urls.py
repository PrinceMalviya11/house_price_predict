from django.contrib import admin
from django.urls import path
from predictor import views

urlpatterns = [
    path("", views.home, name="home"),
    path("house/", views.house_predict, name="house"),
    path("student/", views.predict_student, name="predict_student"),
]