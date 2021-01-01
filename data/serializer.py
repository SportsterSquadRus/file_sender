from rest_framework import serializers
from upload.models import FileClass, Number






class FileListSerializer(serializers.ModelSerializer):
    numbers = serializers.StringRelatedField(many=True)
    class Meta:
        model = FileClass
        fields = ('obj', 'numbers',)

