from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import  APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from .util import views_errros

class Login(APIView):
    authentication_classes = []
    permission_classes = []
    def post(self,request) -> Response:
        try:
            username = request.data["username"]
            password = request.data["password"]
            user = authenticate(username=username,password=password)


            if user is not None:
                token = RefreshToken.for_user(user)
                return Response({"data":{"access_token":str(token.access_token),"refresh_token":str(token),"atroooo":"atrp"}},status=status.HTTP_200_OK)
            else:
                return Response({"data":"username or password Incorect"})
        except Exception as e:
            print(e)
            views_errros.ViewsError().get()


class Register(APIView):
    permission_classes =  []
    authentication_classes = []
    def post(self,request) -> Response:
        try:
            username = request.data["username"]
            password = request.data["password"]
            if User.objects.filter(username=username).exists():
                return Response({"data":"username Is Alerdy Exists"},status=404)
            else:
                user = User.objects.create_user(username=username,password=password)
                return Response({"data":{"created accounts Successfully"}},status=200)
        except:
            views_errros.ViewsError().get()


class Logout(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request) -> Response:
        try:
            refresh = request.data["refresh_token"]
            tokenm = RefreshToken(refresh)
            tokenm.blacklist()
            return Response({"data":{"message":"logout sucessfully"}},status=200)
        except Exception as e:
            print(e)
            views_errros.ViewsError().get()
class UpdateUsername(APIView):
    permission_classes =  [IsAuthenticated]
    authentication_classes =[]
    def post(self,request) -> Response:
        try:
            username1 = request.data["username1"]
            username2 = request.data["username2"]
            user = User.objects.get(username=username1)
            if user.username1 != username2:
                try:
                    user.objects.filter(username=username1).update(username=username2)
                    return Response({"data":{"username":"updated"}},status=status.HTTP_200_OK)
                except:
                    views_errros.ViewsError().get()
        except:
            views_errros.ViewsError().get()
class UpdatePassword(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request) -> Response:
        try:
            username = request.user
            password1 = request.data["password1"]
            password2 = request.data["password2"]
            user = User.objects.get(username=username)
            if password1 != password2:
                user.objects.filter(username=username).update(password=password2)
                return Response({"data":{"message":"success"}},status= status.HTTP_200_OK)
            else:
                views_errros.ViewsError().get()
        except:
            views_errros.ViewsError().get()
class AddEmail(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request) -> Response:
        try:
            email = request.data["email"]
            user = request.user
            user.email = email
            user.save()
            return Response({"data":{"message":{"add Email Successfully !"}}},status=status.HTTP_200_OK)
        except:
            views_errros.ViewsError().get()
class UpdateEmail(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request) -> Response:
        try:
            email = request.data["email"]
            user = User.objects.get(email= email)
            if user.email != email:
                user.objects.filter(email=email).update(email=email)
                return Response({"data":{"message":"Updates Successfully"}},status=status.HTTP_200_OK)
            else:
                views_errros.ViewsError().get()
        except:
            views_errros.ViewsError().get()
class Profile(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request) -> Response:
        try:
            user = request.user
            info = User.objects.get(username=user)
            return Response({"data":{"user":user,"name":info.first_name+ " " + info.last_name}},status=status.HTTP_200_OK)
        except:
            views_errros.ViewsError().get()









