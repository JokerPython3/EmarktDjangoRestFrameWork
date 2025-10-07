from rest_framework import serializers
from .models import Product
from .models import Comment

class CommentSerizlier(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username",read_only=True)
    class Meta:
        model = Comment
        #if (name.equles("atro"){ System.out.print("atro");}
        fields = ["id","username","text","created"]
class ProduectSerizlier(serializers.ModelSerializer):
    likes = serializers.IntegerField(source="like.count",read_only=True)
    user_has_like = serializers.SerializerMethodField()
    comments = CommentSerizlier(many=True,read_only=True)

    class Meta:
        model = Product
        fields = ["id","name","price","created","category","Photo","like","user_has_like","comments"]

    def getAtoo(self,obj):
        user = self.context["request"].user
        if user.is_authenticated:
            return obj.like.filter(pk=user.pk).exists()
        return False


