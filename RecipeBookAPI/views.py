from django.shortcuts import render
from rest_framework import mixins, viewsets

from .models import *
from .serializers import *


class CategoryAPI(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class RecipeAPI(viewsets.ReadOnlyModelViewSet):

    serializer_class = RecipeSerializer

    def get_queryset(self):
        queryset = Recipe.objects.all()
        cat = self.request.query_params.get('cat')
        if cat is not None:
            queryset = queryset.filter(cat_id__pk=cat)
        return queryset

