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

class GenderList(generics.ListCreateAPIView):
    serializer_class = GenderSerializer
    queryset = Gender.objects.all()
    name = 'gender-list'

class GenderDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = GenderSerializer
    queryset = Gender.objects.all()
    name = 'gender-detail'

class TitleList(generics.ListCreateAPIView):
    serializer_class = TitleSerializer
    queryset = Title.objects.all()
    name = 'title-list'

class TitleDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TitleSerializer
    queryset = Title.objects.all()
    name = 'title-detail'

class TitleStarringList(generics.ListCreateAPIView):
    serializer_class = TitleStarringSerializer
    name = 'title-starring-list'
    queryset = Starring.objects.all()

class ApiRoot(APIView):
    name = 'api-root'
    
    def get(self, request, *args, **kwargs):
        return Response({
            'starrings': reverse(StarringList.name, request=request),
            'titles': reverse(TitleList.name, request=request),
            'genders': reverse(GenderList.name, request=request),
            'starring-titles': reverse(TitleStarringList.name, request=request)
        })