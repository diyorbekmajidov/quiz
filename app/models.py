from django.db import models

# Create your models here.
class Quiz1(models.Model):
    title=models.CharField(max_length=255)
    def __str__(self):
        return self.title

class Topic(models.Model):
    quiz=models.ForeignKey(Quiz1, on_delete=models.CASCADE)
    t_name=models.CharField(max_length=26)
    def __str__(self):
        return self.t_name

class Question(models.Model):
    question=models.CharField(max_length=255)
    t_name=models.ForeignKey(Topic, on_delete=models.CASCADE)

    def __str__(self):
        return self.question

class Option(models.Model):
    option=models.CharField(max_length=255)
    is_right=models.BooleanField(default=False)
    question=models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.option

class User(models.Model):
    username=models.CharField(max_length=16)
    email=models.EmailField()
    password=models.CharField(max_length=12)
    firstname=models.CharField(max_length=255)
    lastname=models.CharField(max_length=16)
    admin=models.BooleanField(default=False)

    def __str__(self):
        return self.username

class Result(models.Model):
    user_id=models.ForeignKey(User, on_delete=models.CASCADE)
    quiz_title=models.CharField(max_length=255)
    result_detailt_id=models.CharField(max_length=16)

    def __str__(self):
        return self.quiz_title

class Result_detail(models.Model):
    question_name=models.CharField(max_length=255)
    is_solved=models.BooleanField(default=False)
    result_detail_id=models.ForeignKey(Result, on_delete=models.CASCADE)

    def __str__(self):
        return self.question_name






