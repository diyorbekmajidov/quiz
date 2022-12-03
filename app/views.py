from django.shortcuts import render

# from rest_framework import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request

from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication,BasicAuthentication

from .models import Question,Quiz,Option,Result,Result_detail,User
from .serializers import Questionserializer,Quizserializer,Optionserializer

class Quiz(APIView):
    permission_classes = [IsAuthenticated]
    # quiz=Quiz.objects.all()
    # serializer=Quizserializer(quiz,many=True)
    def post(self, request: Request):
        """ 
        Create a new quiz
        """
        serializer=Quizserializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)