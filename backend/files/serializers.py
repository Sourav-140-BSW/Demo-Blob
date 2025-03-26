from rest_framework import serializers
from .models import UploadedFile

class FileSerializer(serializers.ModelSerializer):
    file = serializers.FileField()  # ✅ Explicitly define file field

    class Meta:
        model = UploadedFile
        fields = '__all__'
