from django.shortcuts import render
from .models import Video, Activity

# Create your views here.
from rest_framework import viewsets
from .serializers import VideoSerializer, ActivitySerializer


class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer


class ActivityViewSet(viewsets.ModelViewSet):
    serializer_class = ActivitySerializer

    def get_queryset(self):
        queryset = Activity.objects.all()
        id = self.request.query_params.get('id')
        if id is not None:
            queryset = Activity.objects.filter(id=id)
        return queryset
