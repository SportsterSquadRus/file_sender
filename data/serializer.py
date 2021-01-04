from rest_framework import serializers
from upload.models import FileClass


class FileListSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileClass
        fields = ('obj', 'numbers')

