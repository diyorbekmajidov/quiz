from rest_framework import serializers
from .models import Result,Result_detail,Option,User,Question,Quiz1,Topic

class Quizserializer(serializers.ModelSerializer):
    class Meta:
        model=Quiz1
        fields = '__all__'

class Topicserializers(serializers.ModelSerializer):
    class Meta:
        model = Topic
        quiz=serializers.PrimaryKeyRelatedField(queryset=Quiz1.objects.all())
        fields = '__all__'

class Questionserializer(serializers.ModelSerializer):
    class Meta:
        model=Question
        t_name=serializers.PrimaryKeyRelatedField(queryset=Topic.objects.all())
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




