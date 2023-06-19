from django.shortcuts import render
from rest_framework import viewsets
from .models import Post, Directory
from .serializers import PostSerializer, DirectorySerializer
from rest_framework.response import Response


# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        print(request.data)
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save()

    def partial_update(self, request, *args, **kwargs):
        print(request.data)
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)


class DirectoryViewSet(viewsets.ModelViewSet):
    serializer_class = DirectorySerializer
    queryset = Directory.objects.all()
