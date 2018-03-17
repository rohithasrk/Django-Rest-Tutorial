from snippets.models import Snippet
from snippets.serializers import SnippetSerializer, UserSerializer
from django.contrib.auth.models import User
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics


class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
