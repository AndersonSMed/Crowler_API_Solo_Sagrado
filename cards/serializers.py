from rest_framework import serializers
from . import models

class General(serializers.ModelSerializer):

    class Meta:
        model = models.Cards
        exclude = ['mais_recente',]