from django.shortcuts import render
from django.db.models import Q
from rest_framework import viewsets
from .models import Movie
from .serializers import MovieSerializer


# def movieSerach(request):
#     query = request.GET.get('q')
#     if query:
#         movies = Movie.objects.filter(
#             Q(title__icontains=query) |
#             Q(genre__icontains=query) |
#             Q(director__icontains=query)
#         ).distinct()
#     else:
#         movies = Movie.objects.all()
#     return render
class MovieViewSet(viewsets.ModelViewSet):
    template_name = 'addsearch/src/index.js'
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
