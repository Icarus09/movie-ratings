from .models import *
from rest_framework import serializers
from django.contrib.auth.models import User

class StarringSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Starring
        fields = ('name', 'age', 'nationality')

class TitleSerializer(serializers.HyperlinkedModelSerializer):
    starring = serializers.SlugRelatedField(slug_field='name', queryset=Starring.objects.all())
    gender = serializers.SlugRelatedField(slug_field='name', queryset=Gender.objects.all())

    class Meta:
        model = Title
        fields = ('url', 'name', 'gender', 'year', 'starring', )

class GenderSerializer(serializers.HyperlinkedModelSerializer):
    titles = TitleSerializer(read_only=True, many=True)

    class Meta:
        model = Gender
        fields = ('pk', 'name', 'titles')

class TitleStarringSerializer(serializers.HyperlinkedModelSerializer):
    starrings = TitleSerializer(many=True, read_only=True)

    class Meta:
        model = Starring
        fields = ('name', 'age', 'starrings')

class ProfileSerializer(serializers.HyperlinkedModelSerializer):

    def create(self, validated_data):
        user_created = User.objects.create_user(username=validated_data['name'],
                                                email=validated_data['email'],
                                                password='senha')
        return Profile.objects.create(user=user_created, **validated_data)
    
    class Meta:
        model = Profile
        fields = ('name', 'email')

class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('url', 'pk', 'username', 'email')

class RatingSerializer(serializers.HyperlinkedModelSerializer):
    title = serializers.SlugRelatedField(queryset=Title.objects.all(), slug_field='name')
    profile = serializers.SlugRelatedField(queryset=Profile.objects.all(), slug_field='name')

    class Meta:
        model = Rate
        fields = ('note', 'profile', 'title')