from rest_framework import serializers
from .models import  cricketTeamsModel

class teamSerializer(serializers.Serializer):

    class meta():
        model = cricketTeamsModel
        fields = '__all__'


