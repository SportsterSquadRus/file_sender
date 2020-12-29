from django.urls import path
from .views import upload_file



urlpatterns = [
    path('api', upload_file),

]
