import os

from django.shortcuts import render

# Create your views here.
from django.views import View


class Home(View):
    def get(self, request):
        # <view logic>
        content = {
            "image": os.listdir("show/static/show")
        }
        return render(request, 'show/home.html', content)
