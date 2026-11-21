from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError
from .serializers import RegisterSerializer, LoginSerializer, LogoutSerializer


class RegisterView(APIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message': 'User registered successfully.'}, status=status.HTTP_201_CREATED)


class LoginView(APIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]
    authentication_classes = []

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(request,username=serializer.validated_data['username'],password=serializer.validated_data['password'],)

        if user is None:
            return Response({'error': 'Invalid credentials.'}, status=401)

        refresh = RefreshToken.for_user(user)
        return Response({'access': str(refresh.access_token),'refresh': str(refresh),})


class LogoutView(APIView):
    serializer_class = LogoutSerializer
    permission_classes = [AllowAny]
    authentication_classes = []

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            refresh = RefreshToken(serializer.validated_data['refresh'])
            refresh.blacklist()
        except TokenError:
            return Response({'error': 'Invalid or expired refresh token.'}, status=401)
        return Response({'message': 'Logout successful.'})
