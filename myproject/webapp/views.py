from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from . models import *
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.db import IntegrityError
from . serializer import RoomSerializer
from rest_framework import generics, status, permissions, mixins
from rest_framework.exceptions import ValidationError
from .serializer import *


 

@csrf_exempt
def login(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        user = authenticate(
            request, username=data['username'], password=data['password'])
        if user is None:
            return JsonResponse({'error': 'Please Check user name and password and try again'}, status=400)
        else:
            try:
                token = Token.objects.get(user=user)
            except:
                token = Token.objects.create(user=user)
            return JsonResponse({'token': str(token), 'username': data['username']}, status=200)


class Sign(APIView):
    def post(self,request):
        serializers = SignSerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({'error': False}) 
        return Response({'error': True})

# @csrf_exempt
# def signup(request):
#     if request.method == 'POST':
#         try:
            
#             data = JSONParser().parse(request) 
#             user = User.objects.create_user(
#                 data['username'], password=data['password'])
#             user.save()
#             token = Token.objects.create(user=user)
#             return JsonResponse({'token': str(token), 'username': data['username']}, status=201)
#         except IntegrityError:
#             return JsonResponse({'error': 'This UserName is already taken, Please choose a new username'}, status=400)


class RoomList(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [
       permissions.IsAuthenticated
    ]


    def perform_create(self, serializer):
        serializer.save(poster=self.request.user)

class RoomRetriveDestroy(generics.RetrieveDestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    def delete(self, request, *args, kwargs):
        post = Room.objects.filter(pk=kwargs['pk'], poster=self.request.user)
        if post.exists():
            return self.destroy(request, *args, kwargs)
        else:
            raise ValidationError('Thats not your post to delete')