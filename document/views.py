from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .serializers import *
from rest_framework.filters import SearchFilter
from .permissions import IsSuperUserOrReadOnly,FilterObjectPermission


class DocumentModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsSuperUserOrReadOnly,FilterObjectPermission]
    serializer_class = DocumentSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title']

    def get_queryset(self):
        group = self.request.user.groups.all()[0].name
        if group == 'general':
            docs = Document.objects.filter(document_root__in=['public','private','secret'],status='active')
        if group == 'president':
            docs = Document.objects.all()
        if group == 'sergeant':
            docs = Document.objects.filter(document_root__in=['public','private'],status='active')
        if group == 'user':
            docs = Document.objects.filter(document_root__in=['public'],status='active')
        return docs

    def perform_create(self,serializer):
        serializer.save(user=self.request.user)


