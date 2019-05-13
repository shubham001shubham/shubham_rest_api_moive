from django.shortcuts import render
from rest_framework import generics,viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from .serializers import  (MovieSerializer, MovieGenSerializer,
UserSerializer, ChoiceSerializer)
from .models import Gener, Movie
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly,  IsAuthenticated
#from rest_framework.response import Response
#from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404




class ChoiceListMovie(generics.ListCreateAPIView):
    authentication_class = [TokenAuthentication,SessionAuthentication,BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        queryset = Movie.objects.filter(id=self.kwargs["pk"])
        return queryset
    serializer_class = ChoiceSerializer

class MovieCreate(generics.CreateAPIView):
    authentication_class = [TokenAuthentication,SessionAuthentication,BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = MovieSerializer

class MovieList(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieGenSerializer


# blow code to create admin account.
class UserCreate(generics.CreateAPIView):
    authentication_class = ()
    permission_class = ()
    serializer_class = UserSerializer

#below class for login admin
class LoginView(APIView):
    permission_classes = ()
    def post(self,request,):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username,password=password)
        if user:
            return Response({"token":user.auth_token.key})
        else:

            return Response({"error":"Wrong Credentials"},status=status.HTTP_400_BAD_REQUEST)

#below code for serach Movie by Name.
from django_filters.rest_framework import DjangoFilterBackend
class Temp(generics.ListAPIView):
    serializer_class = MovieGenSerializer
    queryset = Movie.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('name',)




# Create your views here.


class SnippetDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    authentication_class = [TokenAuthentication,SessionAuthentication,BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def get_object(self, pk):
        try:
            return Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = MovieGenSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = Movie.objects.get(pk=pk)
        serializer = MovieSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
