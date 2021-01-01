from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from upload.models import FileClass
from .serializer import FileListSerializer

class FilesListView(APIView):
    def get(self, request):
        files = FileClass.objects.all()
        serializer = FileListSerializer(files, many=True)
        return Response(serializer.data)
