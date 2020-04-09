from django.urls import path
from . import views

# path 四个参数：
# route 网址路径 view 视图函数 kwargs name 模块调用别名
urlpatterns = [
    path('', views.index, name='index'),
]
