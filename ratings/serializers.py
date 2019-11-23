from .models import *
from rest_framework import serializers

class StarringSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Starring
        fields = ('name', 'age')

class TitleSerializer(serializers.HyperlinkedModelSerializer):
    starring = serializers.SlugRelatedField(slug_field='name', queryset=Starring.objects.all())

    class Meta:
        model = Title
        fields = ('name', 'year', 'starring')