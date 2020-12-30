from django.urls import path
from .views import upload_file, FilesListView



urlpatterns = [
    path('api/', upload_file),
    path('list/', FilesListView.as_view(), name='list_url')

]
