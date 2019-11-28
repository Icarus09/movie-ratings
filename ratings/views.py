from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.authentication import SessionAuthentication
from .serializers import *
from .permissions import *

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

#todo: modificar depois
class TitleStarringList(generics.ListCreateAPIView):
    serializer_class = TitleStarringSerializer
    name = 'title-starring-list'
    queryset = Starring.objects.all()

class ProfileList(generics.ListCreateAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    name = 'profile-list'

class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    name = 'profile-detail'

class UserList(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    name = 'user-list'
    permission_classes = (permissions.IsAuthenticated,)

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    name = 'user-detail'

class RatingList(generics.ListCreateAPIView):
    serializer_class = RatingSerializer
    queryset = Rate.objects.all()
    name = 'rate-list'
    permission_classes = (IsUserOrReadOnly, permissions.IsAuthenticatedOrReadOnly)

class RatingDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RatingSerializer
    queryset = Rate.objects.all()
    name = 'rate-detail'
    permission_classes = (IsUserOrReadOnly,)

class ApiRoot(APIView):
    name = 'api-root'
    
    def get(self, request, *args, **kwargs):
        return Response({
            'users': reverse(UserList.name, request=request),
            'starrings': reverse(StarringList.name, request=request),
            'titles': reverse(TitleList.name, request=request),
            'genders': reverse(GenderList.name, request=request),
            'starring-titles': reverse(TitleStarringList.name, request=request),
            'profile-list': reverse(ProfileList.name, request=request),
            'ratings': reverse(RatingList.name, request=request)
        })