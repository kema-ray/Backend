from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from authentication.serializers import *
from rest_framework import status,response
from django.contrib.auth import authenticate

class RegisterAPIView(GenericAPIView):

    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status = status.HTTP_201_CREATED)

        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginAPIView(GenericAPIView):

    def post(self, request):
        email = request.data.get('email', None)
        password = request.date.get('password', None)

        user = authenticate(username = email, password = password)

        if user:
            pass