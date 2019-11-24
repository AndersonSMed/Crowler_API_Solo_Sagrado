from rest_framework import serializers
from . import models

class General(serializers.ModelSerializer):

    def create(self, validated_data):
        
        models.Cards.objects.filter(
            titulo = validated_data.get('titulo')
        ).update(mais_recente = False)

        return models.Cards.objects.create(**validated_data)

    class Meta:
        model = models.Cards
        exclude = ['mais_recente',]