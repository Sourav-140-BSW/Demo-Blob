# from rest_framework import generics
# from rest_framework.response import Response
# from rest_framework.parsers import MultiPartParser, FormParser
# from django.http import FileResponse
# from django.utils.encoding import smart_str
# from .models import UploadedFile
# from .serializers import FileSerializer

# # ✅ Upload File View (Handles POST requests)
# from rest_framework import generics
# from rest_framework.parsers import MultiPartParser, FormParser
# from .models import UploadedFile
# from .serializers import FileSerializer

# class FileUploadView(generics.CreateAPIView):
#     queryset = UploadedFile.objects.all()
#     serializer_class = FileSerializer
#     parser_classes = (MultiPartParser, FormParser)  # ✅ Ensures handling of multipart/form-data


# # ✅ List All Files
# class FileListView(generics.ListAPIView):
#     queryset = UploadedFile.objects.all()
#     serializer_class = FileSerializer

# # ✅ Download File
# class FileDownloadView(generics.RetrieveAPIView):
#     queryset = UploadedFile.objects.all()
#     serializer_class = FileSerializer

#     def get(self, request, *args, **kwargs):
#         file_obj = self.get_object()
#         response = FileResponse(file_obj.file, as_attachment=True)
#         response['Content-Disposition'] = f'attachment; filename="{smart_str(file_obj.name)}"'
#         return response


# files/views.py
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from django.http import FileResponse
from django.utils.encoding import smart_str
from .models import UploadedFile
from .serializers import FileSerializer
from .utils import upload_to_azure_blob, delete_from_azure_blob
import requests

class FileUploadView(generics.CreateAPIView):
    queryset = UploadedFile.objects.all()
    serializer_class = FileSerializer
    parser_classes = (MultiPartParser, FormParser)

    def create(self, request, *args, **kwargs):
        file_obj = request.FILES.get('file')
        if not file_obj:
            return Response({'error': 'No file provided'}, status=status.HTTP_400_BAD_REQUEST)

        # Upload to Azure Blob Storage
        upload_result = upload_to_azure_blob(file_obj)
        if not upload_result:
            return Response({'error': 'Failed to upload to Azure'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        # Create database record
        file_data = {
            'name': upload_result['original_name'],
            'azure_url': upload_result['url'],
            'azure_filename': upload_result['filename'],
            'file_size': upload_result['size']
        }
        
        serializer = self.get_serializer(data=file_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class FileListView(generics.ListAPIView):
    queryset = UploadedFile.objects.all()
    serializer_class = FileSerializer

class FileDownloadView(generics.RetrieveAPIView):
    queryset = UploadedFile.objects.all()
    serializer_class = FileSerializer

    def get(self, request, *args, **kwargs):
        file_obj = self.get_object()
        # Redirect to Azure Blob URL for download
        return Response({
            'url': file_obj.azure_url,
            'name': file_obj.name
        })

class FileDeleteView(generics.DestroyAPIView):
    queryset = UploadedFile.objects.all()
    serializer_class = FileSerializer

    def perform_destroy(self, instance):
        # Delete from Azure first
        if delete_from_azure_blob(instance.azure_filename):
            instance.delete()
        else:
            raise Exception("Failed to delete file from Azure Blob Storage")