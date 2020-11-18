from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def work01(request):
    message = "Hello Django"
    return HttpResponse(message)


def work02(request):
    message = "Hello02"
    return HttpResponse(message)


def work03(request):
    message = "<html><body><h1>Hello03</h1></body></html>"
    return HttpResponse(message)


def work04(request):
    message = """
<html>
    <body>
        <h1>Fruits</h1>
        <ul>
            <li>apple</li>
            <li>orange</li>
            <li>melon</li>
        </ul>
    </body>
</html>"""
    return HttpResponse(message)


def work05(request):
    html = """
<html>
    <body>
        <h1>生徒一覧</h1>
        <ul>
            <li>ジョン</li>
            <li>ナンシー</li>
            <li>ボブ</li>
        </ul>
    </body>
</html>"""
    return HttpResponse(html)


def work06(request):
    html = """
<html>
    <body>
        <h1>今日の天気</h1>
        <h2>晴れのち曇り</h2>
        <h3>最高気温：30度</h3>
        <h3>最低気温：21度</h3>
    </body>
</html>"""
    return HttpResponse(html)
