# from rest_framework import serializers
# from .models import UploadedFile

# class FileSerializer(serializers.ModelSerializer):
#     file = serializers.FileField()  # ✅ Explicitly define file field

#     class Meta:
#         model = UploadedFile
#         fields = '__all__'


# files/serializers.py
from rest_framework import serializers
from .models import UploadedFile

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadedFile
        fields = '__all__'
        read_only_fields = ('azure_url', 'azure_filename', 'file_size', 'uploaded_at')