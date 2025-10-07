from django.urls import path

from accounts.util.views_errros import ViewsError
from . import views

urlpatterns = [
    path('api/auth/products/show/',views.Show.as_view(),name="atro"),
    path("api/auth/serach/name/",views.Serch_name.as_view(),name="serche"),
    path("api/auth/search/price/",views.Atro.as_view(),name="ss"),
    path("api/auth/search/catogry",views.Ntro.as_view(),name="nnn"),
    path("api/auth/like/product/<int:pk>/",views.Like.as_view(),name="like"),
    path("api/auth/comment/atro/ntro/ss/<int:id>/",views.CommentAtroC.as_view()),
    path("api/auth/comment/ss/<int:id>/",views.DAndUCommentr.as_view())

]
handler404 = ViewsError().get()
handler500 =ViewsError().get()