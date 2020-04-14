from django.urls import path
from . import views

# path 四个参数：
# route 网址路径 view 视图函数 kwargs name 模块调用别名
app_name = 'polls'
# urlpatterns = [
#     path('', views.index, name='index'),
#     path('<int:question_id>/', views.detail, name='detail'),
#     path('<int:question_id>/results/', views.results, name='detail'),
#     path('<int:question_id>/vote/', views.vote, name='vote'),
#
# ]

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:pk>/vote/', views.vote, name='vote'),
]