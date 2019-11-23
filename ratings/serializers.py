from .models import *
from rest_framework import serializers

class StarringSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Starring
        fields = ('name', 'age')
