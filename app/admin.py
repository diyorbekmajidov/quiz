from django.contrib import admin

# Register your models here.
from .models import Question,Quiz1,User,Result,Result_detail,Option,Topic

admin.site.register(Quiz1)
admin.site.register(Topic)
admin.site.register(Question)
admin.site.register(User)
admin.site.register(Result)
admin.site.register(Result_detail)
admin.site.register(Option)