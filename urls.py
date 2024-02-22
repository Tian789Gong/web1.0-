""" 定义learning_logs的URL模式"""


from django.urls import path, re_path
from . import views

app_name = 'learning_logs'
# 变量urlpatterns是一个列表，包含可在应用程序learning_logs中请求的网页
urlpatterns = [
# 主页
    path('',views.index, name='index'),
    re_path(r'^topics/$', views.topics, name='topics'),
]
         




 

