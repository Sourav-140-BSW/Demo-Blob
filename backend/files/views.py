from rest_framework import generics
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from django.http import FileResponse
from django.utils.encoding import smart_str
from .models import UploadedFile
from .serializers import FileSerializer

# ✅ Upload File View (Handles POST requests)
from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser
from .models import UploadedFile
from .serializers import FileSerializer

class FileUploadView(generics.CreateAPIView):
    queryset = UploadedFile.objects.all()
    serializer_class = FileSerializer
    parser_classes = (MultiPartParser, FormParser)  # ✅ Ensures handling of multipart/form-data


# ✅ List All Files
class FileListView(generics.ListAPIView):
    queryset = UploadedFile.objects.all()
    serializer_class = FileSerializer

# ✅ Download File
class FileDownloadView(generics.RetrieveAPIView):
    queryset = UploadedFile.objects.all()
    serializer_class = FileSerializer

    def get(self, request, *args, **kwargs):
        file_obj = self.get_object()
        response = FileResponse(file_obj.file, as_attachment=True)
        response['Content-Disposition'] = f'attachment; filename="{smart_str(file_obj.name)}"'
        return response
