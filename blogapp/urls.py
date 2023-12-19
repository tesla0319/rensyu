from django.urls import path
from . import views

#URLconfのURLパターンを逆引きできるようにアプリ名を登録
app_name = 'blogapp'

#URLパターンを登録するためのリスト
urlpatterns = [
    #http(s)://ホスト名/以下のパスが''（無し）の場合
    #viewsモジュールのIndexViewを実行
    #URLパターン名は'index'
    path('',views.IndexView.as_view(),name='index'),
]