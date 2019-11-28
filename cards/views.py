from rest_framework import generics, status
from rest_framework.response import Response
from django.db.models import Q
from . import models, serializers, paginators

class List(generics.ListAPIView):

    serializer_class = serializers.General
    queryset = models.Cards.objects.all()
    pagination_class = paginators.DefaultPaginator
    
    def filter_queryset (self, queryset):
        nome = self.request.query_params.get('nome', None)
        
        if nome is not None:
            queryset = queryset.filter(
                Q(
                    Q(titulo__icontains = nome)
                ),
                mais_recente = True
            )

        return queryset