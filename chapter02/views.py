from django.shortcuts import render

# Create your views here.

def work01(request):
    params = {
        "title" : "work01",
        "message" : "this is work01"
    }
    return render(request, "chapter02/work01.html", params)


def work02a(request):
    params = {
        "title" : "work02a"
    }
    return render(request, "chapter02/work02a.html", params)


def work02b(request):
    params = {
        "title" : "work02b"
    }
    return render(request, "chapter02/work02b.html", params)


def work03a(request):
    params = {
        "title" : "work03a"
    }
    return render(request, "chapter02/work03a.html", params)


def work03b(request):
    name = request.GET["name"]
    age = request.GET["age"]
    params = {
        "title" : "work03b",
        "data" : {
            "name" : name,
            "age" : age,
        }
    }
    return render(request, "chapter02/work03b.html", params)

def work04a(request):
    params = {
        "title" : "work04a"
    }
    return render(request, "chapter02/work04a.html", params)


def work04b(request):
    # 初期値設定
    data  = {
        "name" : "",
        "age" : "",
    }
    # パラメータがあれば、代入する
    if "name" in request.GET :
        data["name"] = request.GET["name"]
    if "age" in request.GET :
        data["age"] = request.GET["age"]
    
    # テンプレートに渡す変数
    params = {
        "title" : "work04b",
        "data" : data
    }
    return render(request, "chapter02/work04b.html", params)


def work05a(request):
    params = {
        "title" : "work05a"
    }
    return render(request, "chapter02/work05a.html", params)


def work05b(request):
    # 初期値設定
    data  = {
        "name" : "",
        "age" : "",
    }
    # パラメータがあれば、代入する
    if "name" in request.POST :
        data["name"] = request.POST["name"]
    if "age" in request.POST :
        data["age"] = request.POST["age"]
    
    # テンプレートに渡す変数
    params = {
        "title" : "work05b",
        "data" : data
    }
    return render(request, "chapter02/work05b.html", params)


def work06(request):
    # 初期値設定
    data  = {
        "name" : "",
        "age" : "",
    }
    if request.method == "POST" :
        # パラメータがあれば、代入する
        if "name" in request.POST :
            data["name"] = request.POST["name"]
        if "age" in request.POST :
            data["age"] = request.POST["age"]
    # テンプレートに渡す変数
    params = {
        "title" : "work06",
        "data" : data
    }
    print(params)
    return render(request, "chapter02/work06.html", params)


def work07(request):
    # 初期値設定
    data  = {
        "city" : ""
    }
    if request.method == "POST" :
        # パラメータがあれば、代入する
        if "city" in request.POST:
            data["city"] = request.POST.get("city")
    # テンプレートに渡す変数
    params = {
        "title" : "work07",
        "data" : data
    }
    return render(request, "chapter02/work07.html", params)


def work08(request):
    # 初期値設定
    data  = {
        "music": ""
    }
    if request.method == "POST" :
        # パラメータがあれば、代入する
        if "music" in request.POST:
            data["music"] = request.POST.get("music")
    # テンプレートに渡す変数
    params = {
        "title" : "work08",
        "data" : data
    }
    return render(request, "chapter02/work08.html", params)


def work09(request):
    # 初期値設定
    data  = {
        "movie": []
    }
    if request.method == "POST" :
        # パラメータがあれば、代入する
        if "movie" in request.POST:
            data["movie"] = request.POST.getlist("movie")
    # テンプレートに渡す変数
    params = {
        "title" : "work09",
        "data" : data
    }
    return render(request, "chapter02/work09.html", params)


def work10(request):
    # 初期値設定
    data  = {
        "message" : ""
    }
    if request.method == "POST" :
        # パラメータがあれば、代入する
        if "message" in request.POST:
            data["message"] = request.POST.get("message")
    # テンプレートに渡す変数
    params = {
        "title" : "work09",
        "data" : data
    }
    return render(request, "chapter02/work10.html", params)


def work11(request):
    params = {
        "title" : "work11"
    }
    return render(request, "chapter02/work11.html", params)


def work12(request):
    params = {
        "title" : "work12"
    }
    return render(request, "chapter02/work12.html", params)
