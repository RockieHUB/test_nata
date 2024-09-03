from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Pelatihan
from .serializers import PelatihanSerializer

# Create your views here.
class DashboardAPIView(APIView):
    def get(self, request):
        category = request.query_params.get('category')
        if category:
            pelatihan = Pelatihan.objects.filter(kategori = category)
        else:
            pelatihan = Pelatihan.objects.all()
        serializer = PelatihanSerializer(pelatihan, many=True)
        return Response(serializer.data)