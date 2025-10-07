from django.http import JsonResponse
from rest_framework.response import Response

class ViewsError():
    def __init__(self) -> None:
        self.atro = "atrooooo";__import__("random").choice(["django","Spring","Asp.Net Core","S1","atro"])
    def get(self) -> JsonResponse:
        return JsonResponse({"error":"Try Agine Later"},status=500)



