from rest_framework.decorators import api_view
from rest_framework.viewsets import ModelViewSet
from .models import Project, Measurement
from .serializers import MeasurementSerializer, ProjectSerializer
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED
from rest_framework.response import Response


class ProjectViewSet(ModelViewSet):
    """ViewSet для проекта."""
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    # def project(self, request):
    #     project_queryset = Project.objects.all()
    #     serializer = ProjectSerializer(project_queryset, many=True)
    #     return Response(serializer.data, status=HTTP_200_OK)


class MeasurementViewSet(ModelViewSet):
    """ViewSet для измерения."""
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
