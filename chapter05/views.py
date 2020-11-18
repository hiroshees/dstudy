from django.shortcuts import render
from django.http import HttpRequest
from django.views.generic import TemplateView
from .forms import Work01Form
from .forms import Work02Form

# Create your views here.
class Work01View(TemplateView):
    def __init__(self):
        self.params = {
            "title": "Work01Viewクラス",
            "message" : "",
            "form" : Work01Form(),
        }
    
    def get(self, request):
        return render(request, 'chapter05/work01a.html', self.params)

    def post(self, request):
        self.params["message"] = request.POST["name"]
        self.params["form"] = Work01Form(request.POST)
        return render(request, 'chapter05/work01b.html', self.params)


class Work02View(TemplateView):
    def __init__(self):
        self.params = {
            "title" : "Work02View",
            "message" : "",
            "form" : Work02Form(),
        }
    
    def get(self, request):
        return render(request,"chapter05/work02get.html", self.params)
    
    def post(self, request):
        self.params["message"] = request.POST["name"]
        self.params["form"] = Work02Form(request.POST)
        return render(request, "chapter05/work02post.html", self.params)

    