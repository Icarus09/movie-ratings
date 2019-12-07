from django.shortcuts import render
from rest_framework import generics, status, parsers, renderers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.authentication import SessionAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from django.contrib.auth.models import User
from .serializers import *
from .permissions import *

# Create your views here.
class StarringList(generics.ListCreateAPIView):
    serializer_class = StarringSerializer
    queryset = Starring.objects.all()
    name = 'starring-list'
    permission_classes = (IsAdminReadOnly,)

class StarringDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StarringSerializer
    queryset = Starring.objects.all()
    name = 'starring-detail'
    permission_classes = (IsAdminReadOnly,)

class GenderList(generics.ListCreateAPIView):
    serializer_class = GenderSerializer
    queryset = Gender.objects.all()
    name = 'gender-list'
    permission_classes = (IsAdminReadOnly,)

class GenderDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = GenderSerializer
    queryset = Gender.objects.all()
    name = 'gender-detail'
    permission_classes = (IsAdminReadOnly,)

class TitleList(generics.ListCreateAPIView):
    serializer_class = TitleSerializer
    queryset = Title.objects.all()
    name = 'title-list'
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class TitleDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TitleSerializer
    queryset = Title.objects.all()
    name = 'title-detail'
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsAdminReadOnly)

#todo: modificar depois
class TitleStarringList(generics.ListCreateAPIView):
    serializer_class = TitleStarringSerializer
    name = 'title-starring-list'
    queryset = Starring.objects.all()

class ProfileList(generics.ListCreateAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    name = 'profile-list'
    permission_classes = (IsAdminReadOnly,)

class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    name = 'profile-detail'
    permission_classes = (IsAdminReadOnly,)

class UserList(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    name = 'user-list'
    permission_classes = (permissions.IsAuthenticated, IsUserLogged, IsAdminReadOnly)

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    name = 'user-detail'
    permission_classes = (IsUserLogged, IsAdminReadOnly)

class RatingList(generics.ListCreateAPIView):
    serializer_class = RatingSerializer
    queryset = Rate.objects.all()
    name = 'rate-list'
    permission_classes = (IsUserOrReadOnly, permissions.IsAuthenticatedOrReadOnly, IsAdminReadOnly)

class RatingDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RatingSerializer
    queryset = Rate.objects.all()
    name = 'rate-detail'
    permission_classes = (IsUserOrReadOnly, IsAdminReadOnly)

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

class ObtainToken(APIView):
    throttle_classes = ()
    permission_classes = ()
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = AuthTokenSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            # pdb.set_trace()
            try:
                user = User.objects.get(email=request.data['username'])
                token = jwt.encode({
                    'user_id': user.id,
                    'email': user.email,
                    'iat': datetime.datetime.utcnow(),
                    'exp': datetime.datetime.utcnow() + datetime.timedelta(days=7)
                }, settings.SECRET_KEY)
                return Response({'token': token})
            except User.DoesNotExist:
                pass
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)