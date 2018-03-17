from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class SnippetList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get(self, request, format=None):
        return self.list(request, *args, **kwargs)

    def post(self, request, format=None):
        return self.create(request, *args, **kwargs)


class SnippetDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get(self, request, pk, format=None):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, pk, format=None):
        return self.update(request, *args, **kwargs)

    def delete(self, request, pk, format=None):
        return self.destroy(request, *args, **kwargs)
