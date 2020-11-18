from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpRequest
from django.http import HttpResponse
from django.urls import reverse_lazy

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import(LoginView, LogoutView)
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView
from django.contrib.auth import login

from django.contrib import messages


from .models import CustomUser
from .forms import LoginForm
from .forms import RegisterForm


class LoginView(SuccessMessageMixin, LoginView):
    """
    ログイン画面
    """
    form_class = LoginForm
    template_name = 'registration/login.html'
    success_message = "ログインしました"


class LogoutView(LoginRequiredMixin, LogoutView):
    """
    ログアウト処理
    """
    success_message = "ログアウトしました"
    
    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        messages.success(request, self.success_message)
        return response


class RegisterView(SuccessMessageMixin, CreateView):
    form_class = RegisterForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("chapter07:dashboard")
    success_message = "新規作成しました"

    def form_valid(self, form):
        # formの情報を保存
        user = form.save() 
        # 認証
        login(self.request, user)
        self.object = user 
        # メッセージ代入
        messages.success(self.request, self.success_message)
        # リダイレクト
        return redirect(self.get_success_url()) 


def index(request):
    """
    ログインしなくてもアクセス可能
    """
    return render(request, "chapter07/index.html")


@login_required
def dashboard(request):
    """
    ログイン必須　ダッシュボード
    """
    user = request.user
    print(dir(user))
    return render(request,"chapter07/dashboard.html")
