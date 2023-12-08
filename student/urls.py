
from . import views
from django.urls import path
from student import views



urlpatterns = [
    path('class/', views.ClassDetailAPIView.as_view()),
    path('student/', views.StudentDetailAPIView.as_view()),
    path('student_update/<int:id>/', views.StudentUpadateAPIView.as_view()),
    path('login/', views.LoginAPIView.as_view()),


     ]