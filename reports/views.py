from django.http.response import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from .serializers import ReportSerializer
from .models import Report


class CreateReport(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = ReportSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)

            return Response(serializer.data, status.HTTP_201_CREATED)

        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class GetOrUpdateReport(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self, slug):
        try:
            return Report.objects.get(slug=slug)
        except Report.DoesNotExist:
            return Http404

    def get(self, request, slug, format=None):
        report = self.get_object(slug)
        serializer = ReportSerializer(report)

        return Response(serializer.data)

    def put(self, request, slug, format=None):
        report = self.get_object(slug)
        serializer = ReportSerializer(report, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status.HTTP_201_CREATED)

        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class ListReport(ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Report.objects.all().order_by('pk')
    serializer_class = ReportSerializer
