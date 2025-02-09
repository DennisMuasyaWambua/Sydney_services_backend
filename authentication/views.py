from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import *
from rest_framework import status

# Create your views here.
class RegisterView(APIView):
    serializer_class = UserSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
class LoginView(APIView):
     def post(self, request):
         email = request.data['email']
         password = request.data['password']

         user = authenticate(username=email, password=password)

         if user is None:
             raise AuthenticationFailed("Invalid username or password!")
         
         token = RefreshToken.for_user(user)

         print(token.access_token)

         return Response({
            "status": True,
            "message": "Login Successful",
            'access_token': str(token.access_token),
            'expires_in': '3600',
            'token_type': 'Bearer',
          })
class CreateServiceView(APIView):
     serializer_class = ServicesSerializer
     def post(self, request):
         data = request.data
         serializer = self.serializer_class(data=data)
         serializer.is_valid(raise_exception=True)
         serializer.save()
         return Response(serializer.data,status=status.HTTP_201_CREATED)
     def get(self, request):
         services = Services.objects.all()
         serializer = self.serializer_class(services, many=True)
         return Response(serializer.data, status=status.HTTP_200_OK)
class CreateServiceProvider(APIView):
     serializer_class = ServiceProviderSerializer
     def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
     def get(self, request):
        service_providers = ServiceProvider.objects.all()
        serializer = self.serializer_class(service_providers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
         


         
