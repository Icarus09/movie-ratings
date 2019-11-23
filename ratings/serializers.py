from .models import *
from rest_framework import serializers

class StarringSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Starring
        fields = ('name', 'age', 'nationality')


class TitleSerializer(serializers.HyperlinkedModelSerializer):
    starring = serializers.SlugRelatedField(slug_field='name', queryset=Starring.objects.all())
    gender = serializers.SlugRelatedField(slug_field='name', queryset=Gender.objects.all())

    class Meta:
        model = Title
        fields = ('url', 'name', 'gender', 'year', 'starring')


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