from django.urls import path 
from .views import Quiz,Question,Option

urlpatterns = [
    path('quiz/', Quiz.as_view()),
    path('question/', Question.as_view()),
    path('option/', Option.as_view()),
]