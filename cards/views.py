from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from django.db.models import Q
from . import models, serializers

class List(generics.ListAPIView):

    serializer_class = serializers.General
    queryset = models.Cards.objects.all()
    pagination_class = None
    
    def filter_queryset (self, queryset):
        nome = self.request.query_params.get('nome', None)
        query_size = self.request.query_params.get('query_size', 10)
        
        if nome is not None:
            queryset = queryset.filter(
                Q(
                    Q(titulo__icontains = nome) |
                    Q(codigo__icontains = nome)
                )
            )

        return queryset[:query_size]