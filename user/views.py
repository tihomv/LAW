from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View


class Login(View):
    def get(self, request):
        # <view logic>
        return HttpResponse('result')

