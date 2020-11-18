from django.shortcuts import render

# Create your views here.
def work01(request):
    params = {
        "title" : "ワーク1",
        "data" : {
        }
    }
    if(request.method == "GET"):
        params["data"]["message"] = "this is get"
    elif( request.method == "POST"):
        params["data"]["message"] = "this is post"
    return render(request, "chapter03/work01.html", params)


    