
from . import views
from django.urls import path
from student import views

urlpatterns = [
    path('class/', views.ClassDetailAPIView.as_view()),
    path('student/', views.StudentDetailAPIView.as_view(), name='student'),
    path('student_update/<int:id>/', views.StudentUpadateAPIView.as_view(), name='student_update'),
    path('loginn/', views.LoginAPIView.as_view(),name='loginn'),
    path('home/', views.home, name='home'),

     ]