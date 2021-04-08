from django.http.response import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .serializers import ProjectSerializer
from .models import Project


class CreateProject(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListProject(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request, format=None):
        project = Project.objects.all().order_by('-pk')
        serializer = ProjectSerializer(project)

        return Response(serializer)


class GetOrUpdateProject(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self, slug):
        try:
            return Project.objects.get(slug=slug)
        except Project.DoesNotExist:
            return Http404

    def get(self, request, slug, format=None):
        project = self.get_object(slug)
        serializer = ProjectSerializer(project)

        return Response(serializer.data)

    def put(self, request, slug, format=None):
        project = self.get_object(slug)
        serializer = ProjectSerializer(project, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
