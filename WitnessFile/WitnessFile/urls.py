from django.urls import path
from myapp.views import upload_file  # ✅ Import the view function

urlpatterns = [
    path('upload/', upload_file, name='gridfs-upload'),
]
