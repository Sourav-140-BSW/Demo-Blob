from django.urls import path
from .views import FileUploadView, FileListView, FileDownloadView

urlpatterns = [
    path('files/', FileListView.as_view(), name='file-list'),
    path('files/upload/', FileUploadView.as_view(), name='file-upload'),  # ✅ Only one upload route
    path('files/<int:pk>/', FileDownloadView.as_view(), name='file-download'),
]
