
from django.contrib import admin
from django.urls import path,include
from app.views import Quiz,Question

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls'))
]
