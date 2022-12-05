from django.urls import path 
from .views import Quiz,Question,Option,Topic

urlpatterns = [
    path('quiz/', Quiz.as_view()),
    path('question/', Question.as_view()),
    path('option/', Option.as_view()),
    path('topic/<int:pk>/', Topic.as_view()),
]