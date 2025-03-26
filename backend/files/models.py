# from django.db import models

# class UploadedFile(models.Model):
#     file = models.FileField(upload_to='uploads/')
#     name = models.CharField(max_length=255)
#     uploaded_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.name


# files/models.py
from django.db import models

class UploadedFile(models.Model):
    name = models.CharField(max_length=255)
    azure_url = models.URLField(max_length=500)
    azure_filename = models.CharField(max_length=255, default="temp_default")  # Stores the unique filename in Azure
    file_size = models.IntegerField()
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name