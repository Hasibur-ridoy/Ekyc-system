from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.serializers import Serializer
from .serializers import Student_info_Serializers
from entries.models import *

# Create your views here.
@api_view(['GET'])
def apiOverview(request):
    return JsonResponse("APII BASE POINT", safe=False)
    
@api_view(['GET'])
def apiStudentview(request):
    studnet = Student_info.objects.all()
    student_seriallizer = Student_info_Serializers(studnet, many=True)
    return Response(student_seriallizer.data)