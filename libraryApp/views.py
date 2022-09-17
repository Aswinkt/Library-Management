import imp
from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse
from .serializers import UserSerializer, BookSerializer
from .models import User, Book
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser



# Create your views here.

# using generic api view

# user list
class UserListView(generics.ListAPIView):

    serializer_class = UserSerializer
    queryset = User.objects.all()


# add user
class UserListAdd(generics.ListCreateAPIView):

    serializer_class = UserSerializer
    queryset = User.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, IsAdminUser)


# update user data
class UserListUpdate(generics.RetrieveUpdateAPIView):

    serializer_class = UserSerializer
    queryset = User.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, IsAdminUser)
    lookup_field = 'pk'

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(request.data, status=status.HTTP_200_OK)
        else:
            return Response({"message":"Update Failed"})



# delete user data
class UserListDelete(generics.RetrieveDestroyAPIView):

    serializer_class = UserSerializer
    queryset = User.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, IsAdminUser)



# book list
class BookListView(generics.ListAPIView):

    serializer_class = BookSerializer
    queryset = Book.objects.all()


# add book
class BookListAdd(generics.ListCreateAPIView):

    serializer_class = BookSerializer
    queryset = Book.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, IsAdminUser)


# update book data
class BookListUpdate(generics.RetrieveUpdateAPIView):

    serializer_class = BookSerializer
    queryset = Book.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, IsAdminUser)
    lookup_field = 'pk'

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(request.data, status=status.HTTP_200_OK)
        else:
            return Response({"message":"Update Failed"})



# delete book data
class BookListDelete(generics.RetrieveDestroyAPIView):

    serializer_class = BookSerializer
    queryset = Book.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, IsAdminUser)


