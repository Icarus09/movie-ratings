from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .serializers import *

# Create your views here.
class StarringList(generics.ListCreateAPIView):
    serializer_class = StarringSerializer
    queryset = Starring.objects.all()
    name = 'starring-list'

class StarringDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StarringSerializer
    queryset = Starring.objects.all()
    name = 'starring-detail'

class TitleList(generics.ListCreateAPIView):
    serializer_class = TitleSerializer
    queryset = Title.objects.all()
    name = 'title-list'

class TitleDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TitleSerializer
    queryset = Title.objects.all()
    name = 'title-detail'

class ApiRoot(APIView):
    name = 'api-root'
    
    def get(self, request, *args, **kwargs):
        return Response({
            'starrings': reverse(StarringList.name, request=request),
            'titles': reverse(TitleList.name, request=request),
        })