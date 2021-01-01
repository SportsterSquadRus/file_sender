from django.urls import path
from .views import FilesListView, FileDetialView


urlpatterns = [
    path('list/', FilesListView.as_view()),
    path('<int:pk>', FileDetialView.as_view())

]