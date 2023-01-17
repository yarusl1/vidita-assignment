from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth import authenticate, login
from django.db import IntegrityError
from .models import MyUser


class AuthTest(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user = request.user
        return Response({"name": user.name})


class SignupView(APIView):
    def post(self, request):
        name = request.data.get('name')
        email = request.data.get('email')
        password = request.data.get('password')

        if not name or not email or not password:
            return Response({'error': 'Please provide all the required fields'},
                            status=status.HTTP_400_BAD_REQUEST)

        try:
            user = MyUser.objects.create_user(
                name=name,
                email=email,
                password=password
            )
            user.save()
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key, 'success': 'Account created successfully'},
                            status=status.HTTP_201_CREATED)
        except IntegrityError:
            return Response({'error': 'Email already exists'},
                            status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    authentication_classes = (TokenAuthentication,)

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        user = authenticate(email=email, password=password)

        if user:
            login(request, user)
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key, 'user_id': user.pk, 'name': user.name}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
