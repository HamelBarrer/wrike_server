from django.http.response import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from .serializers import ProfileSerializer
from .models import Profile


class GetPerfil(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self, slug):
        try:
            return Profile.objects.get(slug=slug)
        except Profile.DoesNotExist:
            raise Http404

    def get(self, request, slug, format=None):
        perfil = self.get_object(slug)
        serializer = ProfileSerializer(perfil)
        return Response(serializer.data)
