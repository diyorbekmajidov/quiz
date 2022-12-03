
from django.contrib import admin
from django.urls import path,include
from app.views import Quiz

urlpatterns = [
    path('admin/', admin.site.urls),
    path('quiz/', include('app.urls'))
]
