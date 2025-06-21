from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework.parsers import MultiPartParser
from rest_framework.decorators import api_view, parser_classes
import pymongo
import gridfs

mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")
mongo_db = mongo_client["File"]  # Use your actual DB name
fs = gridfs.GridFS(mongo_db)

@csrf_exempt
@api_view(['POST'])
@parser_classes([MultiPartParser])
def upload_file(request):
    uploaded_file = request.FILES.get('file')
    if not uploaded_file:
        return JsonResponse({'error': 'No file uploaded'}, status=400)
    try:
        # Save the file to GridFS
        file_id = fs.put(
            uploaded_file.read(),
            filename=uploaded_file.name,
            content_type=uploaded_file.content_type
        )
        return JsonResponse({
            'message': 'Success',
            'file_id': str(file_id)
        }, status=201)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
