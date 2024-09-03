from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth.hashers import make_password  
from .serializers import AkunItemSerializer

# Create your views here.
class RegisterAPIView(APIView):
    def post(self, request):
        serializer = AkunItemSerializer(data=request.data)
        if serializer.is_valid():
            password = serializer.validated_data['password']
            hashed_password = make_password(password)
            serializer.validated_data['password'] = hashed_password
            serializer.validated_data['userRole'] = 'user'
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)