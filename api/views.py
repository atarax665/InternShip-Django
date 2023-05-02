from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from rest_framework import generics, permissions, filters
from .models import Artist, Work
from .serializers import ArtistSerializer, WorkSerializer, UserSerializer

class WorkList(generics.ListCreateAPIView):
    serializer_class = WorkSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['artist__name']
    ordering_fields = ['artist__name', 'work_type']

    def get_queryset(self):
        queryset = Work.objects.all()
        artist = self.request.query_params.get('artist', None)
        work_type = self.request.query_params.get('work_type', None)
        if artist is not None:
            queryset = queryset.filter(artist__name=artist)
        if work_type is not None:
            if work_type == "YouTube":
                work_type = 'Y'
            elif work_type == "Instagram":
                work_type = 'I'
            elif work_type == "Other":
                work_type = 'O'
            queryset = queryset.filter(type=work_type)
        return queryset

class WorkDetail(generics.RetrieveAPIView):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class RegisterUser(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]
