from django.urls import path
from .views import FilesListView


urlpatterns = [
    path('data/', FilesListView.as_view())
]