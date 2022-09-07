from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.http.response import HttpResponse,HttpResponseRedirect
from django.contrib.auth import logout,login,authenticate
from django.urls import reverse
from .forms import RegisterForm
# Create your views here.


"""
注销视图
url:logout
"""
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('blog:all_topics'))
"""
注册视图
url:register
"""
def registeruser(request):
    if request.method == 'POST':
        new_user = RegisterForm(data=request.POST)
        if new_user.is_valid():
            user = new_user.save()
            login(request,authenticate(username=user.username,password=request.POST['password1']))
            return HttpResponseRedirect(reverse('blog:all_topics'))
        else:
            return HttpResponse('注册失败')
    else:
        user = RegisterForm()
        return render(request,'user/register.html',context={'form':user})