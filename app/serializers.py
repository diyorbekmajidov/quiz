from rest_framework import serializers
from .models import Result,Result_detail,Option,User,Question,Quiz

class Quizserializer(serializers.ModelSerializer):
    class Meta:
        model=Quiz
        fields = '__all__'

class Questionserializer(serializers.ModelSerializer):
    class Meta:
        model=Question
        title=serializers.PrimaryKeyRelatedField(queryset=Quiz.objects.all())
        fields = '__all__'

class Optionserializer(serializers.ModelSerializer):
    class Meta:
        model=Option
        question = serializers.PrimaryKeyRelatedField(queryset=Question.objects.all())
        fields = '__all__'

# class ResultSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Result
#         fields = '__all__'

# class Result_detailSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Result_detail
#         fields = '__all__'


# class Userserializer(serializers.ModelSerializer):
#     class Meta:
#         model=User
#         fields = '__all__'       




