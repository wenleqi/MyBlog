from django.urls import path
from django.contrib.auth.views import LoginView
from . import views,forms
urlpatterns = [
    path('register/',views.registeruser,name='register'),
    path('logout/',views.logout_view,name='logout'),
    path('login/',LoginView.as_view(form_class = forms.LoginForm,template_name='user/login.html',next_page='blog:all_topics'),name='login')
]
app_name='user'