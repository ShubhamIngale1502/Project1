from rest_framework.decorators import api_view,authentication_classes,permission_classes
from .models import Student
from .serializer import StudSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
import requests

@api_view(http_method_names=('GET','POST'))
# @authentication_classes([JWTAuthentication])
# @permission_classes([IsAuthenticated])
def create_view(request):
    if request.method == 'POST':
        serializer = StudSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'GET':
        obj = Student.objects.all()
        serializer = StudSerializer(obj, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

@api_view(http_method_names=('GET','PATCH','PUT','DELETE'))
# @authentication_classes([JWTAuthentication])
# @permission_classes([IsAuthenticated])
def details(request, pk):
    obj = get_object_or_404( Student,pk=pk)
    if request.method == 'GET':
        serializer = StudSerializer(instance=obj)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    if request.method == 'PUT':
        # obj = get_object_or_404(Student,pk=pk)
        serializer = StudSerializer(data=request.data, instance=obj)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'PATCH':
        # obj = get_object_or_404(Student,pk=pk)
        serializer = StudSerializer(data=request.data, instance=obj, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        # obj = get_object_or_404(Student,pk=pk)
        obj.delete()
        return Response(data=None, status=status.HTTP_404_NOT_FOUND)
    
@api_view()
def fetch_data(request):
    result = requests.get("https://dummyjson.com/carts")
    if result.status_code == 200:
        cards = result.json()
        return Response(data=result.json(), status=status.HTTP_200_OK)
    return Response(data={'detail': 'There is an error'}, status=status.HTTP_400_BAD_REQUEST)