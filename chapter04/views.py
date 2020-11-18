from django.shortcuts import render
from .forms import Work01Form
from .forms import Work03Form
from .forms import Work04Form
from .forms import Work05Form
from .forms import Work06Form
from .forms import Work07Form
from .forms import Work08Form
from .forms import Work09Form


# Create your views here.

def work01(request):
    params = {
        "title" : "Work01",
        "message" : "",
        "form" : Work01Form(),
    }
    if request.method == "POST" :
        params["message"] = "名前：" + request.POST["name"]
        params["form"] = Work01Form(request.POST)
        return render(request, "chapter04/work01b.html", params)
    return render(request, "chapter04/work01a.html", params)


def work02(request):
    params = {
        "title" : "Work02",
        "message" : "",
        "form" : Work01Form(),
    }
    if request.method == "POST" :
        params["message"] = "名前：" + request.POST["name"]
        params["form"] = Work01Form(request.POST)
        return render(request, "chapter04/work02b.html", params)
    return render(request, "chapter04/work02a.html", params)


def work03(request):
    params = {
        "title" : "Work03",
        "message" : "",
        "form" : Work03Form(),
    }
    if request.method == "POST" :
        params["message"] = "名前：" + request.POST["name"]
        params["form"] = Work03Form(request.POST)
        return render(request, "chapter04/work03b.html", params)
    return render(request, "chapter04/work03a.html", params)


def work04(request):
    params = {
        "title" : "Work04",
        "message" : "",
        "form" : Work04Form(),
    }
    if request.method == "POST" :
        params["message"] = "名前：" + request.POST["name"]
        params["form"] = Work04Form(request.POST)
        return render(request, "chapter04/work04b.html", params)
    return render(request, "chapter04/work04a.html", params)


def work05(request):
    params = {
        "title" : "Work05",
        "message" : "",
        "form" : Work05Form(),
    }
    if request.method == "POST" :
        params["message"] = "名前：" + request.POST["name"]
        params["form"] = Work05Form(request.POST)
        return render(request, "chapter04/work05b.html", params)
    return render(request, "chapter04/work05a.html", params)


def work06(request):
    params = {
        "title" : "Work06",
        "message" : "",
        "form" : Work06Form(),
    }
    if request.method == "POST" :
        params["message"] = "名前：" + request.POST["name"]
        params["form"] = Work06Form(request.POST)
        return render(request, "chapter04/work06b.html", params)
    return render(request, "chapter04/work06a.html", params)


def work07(request):
    params = {
        "title" : "work07",
        "message" : "",
        "form" : Work07Form(),
    }
    if request.method == "POST" :
        params["message"] = "名前：" + request.POST["name"]
        params["form"] = Work07Form(request.POST)
        return render(request, "chapter04/work07b.html", params)
    return render(request, "chapter04/work07a.html", params)


def work08(request):
    params = {
        "title" : "work08",
        "message" : "",
        "form" : Work08Form(),
    }
    if request.method == "POST" :
        params["message"] = "名前：" + request.POST["name"]
        params["form"] = Work08Form(request.POST)
        return render(request, "chapter04/work08b.html", params)
    return render(request, "chapter04/work08a.html", params)


def work09(request):
    params = {
        "title" : "work09",
        "message" : "",
        "form" : Work09Form(),
    }
    if request.method == "POST" :
        params["message"] = "名前：" + request.POST["name"]
        params["form"] = Work09Form(request.POST)
        print(request.POST)
        return render(request, "chapter04/work09b.html", params)
    return render(request, "chapter04/work09a.html", params)
