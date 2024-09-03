from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Enrollment
from .serializers import EnrollmentSerializer

# Create your views here.
class PelatihankuAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        pelatihan = Enrollment.objects.all()
        serializer = EnrollmentSerializer(pelatihan, many=True)
        return Response(serializer.data)