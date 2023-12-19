from django.shortcuts import render
#django.views.generic.baseからtemplateViewをインポート
from django.views.generic.base import TemplateView

class IndexView(TemplateView):
    '''トップページのビュー

    テンプレートのレンダリングに特化したTemplateViewを継承

    Attributes:
        template_name:レンダリングするテンプレート
    '''

#index.htmlをレンダリングする
    template_name='index.html'