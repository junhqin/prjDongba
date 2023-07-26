from django.shortcuts import render
from rest_framework.views import APIView
# Create your views here.
# 主页
class IndexView(APIView):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')
