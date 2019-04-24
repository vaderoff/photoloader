from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import PhotoSerializer
from .models import Photo
from rest_framework import status
from datetime import datetime


class PhotoViewSet(viewsets.ViewSet):
    def list(self, request):
        date = request.GET.get('date')
        if date:
            date = datetime.strptime(date, '%Y-%m-%d')

        size = request.GET.get('size') or 100
        size = int(size)
        
        queryset = Photo.objects.all()[:size]
        if date:
            queryset = Photo.objects.filter(date=date)[:size]
        serializer = PhotoSerializer(queryset, many=True)
        return Response(serializer.data)

    def load(self, request):
        serializer = PhotoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
