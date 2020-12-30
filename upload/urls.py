from django.urls import path
from .views import upload_file, FilesListView, FileDetailView



urlpatterns = [
    path('api/', upload_file),
    path('list/', FilesListView.as_view(), name='list_url'),
    path('<int:pk>/', FileDetailView.as_view(), name='detail_url')

]
