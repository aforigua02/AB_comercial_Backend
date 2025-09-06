from django.shortcuts import render
from django.db.models import Q
from rest_framework import viewsets
from .models import Vehicle
from .serializers import VehicleSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
class VehicleViewSet(viewsets.ModelViewSet):
    serializer_class = VehicleSerializer

    def get_queryset(self):
        queryset = Vehicle.objects.all().order_by('-created_at')
        search = self.request.query_params.get('q')
        if search:
            queryset = queryset.filter(
                Q(brand__icontains=search) |
                Q(arrival_location__icontains=search) |
                Q(applicant__icontains=search)
            )
        return queryset

@api_view(['GET'])
def health(request):
    return Response({"status": "ok"})