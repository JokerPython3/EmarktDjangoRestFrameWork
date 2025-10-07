from django.shortcuts import render, get_object_or_404

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from emarkt.models import Product
from rest_framework import serializers
from .models import Comment
from emarkt.serilzier import ProduectSerizlier, CommentSerizlier
from rest_framework import generics

# Create your views here.

class Show(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset =Product.objects.all()

    serializer_class =  ProduectSerizlier
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["request"] = self.request
        return context
class Serch_name(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request) -> Response:
        try:
            name = request.data["name"]
            queryset = Product.objects.filter(name=name)
            ser = ProduectSerizlier(queryset,many=True)
            return Response({"data":ser.data},status=200)
        except:
            return Response({"error":{"not found"}},status=404)
class Atro(APIView):
    permission_classes =  [IsAuthenticated]
    def post(self,request) -> Response:
        try:
            price = request.data["price"]
            queryset = Product.objects.filter(price=price)
            ntro = ProduectSerizlier(queryset,many=True)
            return Response({"data":ntro.data},status=200)
        except:
            return Response({"error": {"not found"}}, status=404)
class Ntro(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request) -> Response:
        try:
            cat = request.data["category"]
            queryset = Product.objects.filter(category=cat)
            k= ProduectSerizlier(queryset,many=True)
            return Response({"data":k.data},status=200)
        except:
            return Response({"error":{"not found"}},status=200)

class Like(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request,pk) -> Response:
        like = get_object_or_404(Product,pk=pk)
        user = request.user
        if like.like.filter(pk=user.pk).exists():
            like.like.remove(user)
            liked = False
        else:
            like.like.add(user)
            liked = True
        return Response({"data":{"liked":liked,"like_count":like.like.count()}},status=200)
class CommentAtroC(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CommentSerizlier
    def ntro(self):
        id =self.kwargs["id"]
        return Comment.objects.filter(id=id).order_by("-id")
    def atro(self):
        id = self.kwargs["id"]
        serializers.save(user=self.request.user,id=id)
class DAndUCommentr(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CommentSerizlier
    queryset =  Comment.objects.all()
    def update(self,serializer):
        if self.request.user != self.get_object().user:
            return Response({"error":{"d"}},status=401)
        serializer.save()
    def delete(self, request, *args, **kwargs):
        comment = self.get_object()
        if request.user != comment.user:
            return Response({"data":{"d"}},status=403)
        comment.delete()
        return Response({"data":{"success"}},status=204)







