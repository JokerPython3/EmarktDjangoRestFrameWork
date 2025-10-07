from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()
class Category(models.Model):
    name = models.CharField(max_length=100)

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey("Category",on_delete=models.CASCADE)
    Photo = models.ImageField(upload_to="Photos/",blank=True)
    like = models.ManyToManyField(User,blank=True,related_name="like")
    def like_count(self):
        return self.like.count()
    def __str__(self):
        return self.name
class Comment(models.Model):
    pro = models.ForeignKey(Product,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return "{}: {}".format(self.user.username,self.text[:30])



