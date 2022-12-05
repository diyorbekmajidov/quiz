from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status

from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication,BasicAuthentication

from .models import Question,Quiz1,Option,Result,Result_detail,User,Topic
from .serializers import Questionserializer,Quizserializer,Optionserializer,Topicserializers

class Quiz(APIView):
    permission_classes = [IsAuthenticated]
    def get(slef, request: Request):
        quiz=Quiz1.objects.all()
        serializer=Quizserializer(quiz, many=True)
        return Response(serializer.data)
    
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

class Topic(APIView):
    def get(self, request:Request, pk):
        topik=Topic.objects.all(id=pk)
        serializer = Topicserializers(topik, many=True)
        return Response(serializer.data)

class Question(APIView):
    permission_classes = [IsAuthenticated]

    def post(self ,request:Request):
        serializer = Questionserializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class Option(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request:Request):
        serializer = Optionserializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_204_NO_CONTENT)

# class Reslut(APIView):
#     permission_classes = [IsAuthenticated]
    