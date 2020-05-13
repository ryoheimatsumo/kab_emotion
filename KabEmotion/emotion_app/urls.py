from django.contrib import admin
from django.urls import path
from emotion_app import views

app_name = 'emotion_app'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('emotion/',views.emotion,name='emotion'),
]
