from django.shortcuts import render
from .models import Users
from .serializers import UsersSerializer
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status, exceptions
from django.contrib.auth import authenticate
from rest_framework.authtoken.views import ObtainAuthToken



# EndPoint To Register a New User 

class UserSignUP(generics.ListCreateAPIView):
    serializer_class = UsersSerializer
    queryset = Users.objects.all()

    def post(self, request, format=None):
        serializer = UsersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# EndPoint To LogIn 

class LogInView(ObtainAuthToken):
    pass



