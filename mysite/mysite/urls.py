"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views
from django.conf.urls import url

urlpatterns = [
	url(r'^admin/', admin.site.urls),
	#計算本利和
    url(r'^go/$', views.pylinkweb),  #新增這一列
	url(r'^fv/', views.deposits),   #新增這一列 
	url(r'^result/$', views.result),   #新增這一列 
    #公司股票
    url(r'^company/$', views.company),
    url(r'^company/insert/$', views.insert),
    url(r'^do_insert/$', views.do_insert),
    url(r'^company/detail/(?P<stockid>\d+)/$', views.detail), #動態網頁資料
    url(r'^company/update/(?P<stockid>\d+)/$', views.update),
    url(r'^do_update/$', views.do_update),
    url(r'^company/delete/(?P<stockid>\d+)/$', views.delete),
    url(r'^do_delete/$', views.do_delete),




]
