from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer, RoleSerializer

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

         user = authenticate(email=email, password=password)

         if user is None:
             raise AuthenticationFailed("Invalid username or password!")
         
         token = RefreshToken.for_user(user)

         return Response({
            "status": True,
            "message": "Login Successful",
            'access_token': str(token.access_token),
            'expires_in': '3600',
            'token_type': 'Bearer',
          })
         


         
