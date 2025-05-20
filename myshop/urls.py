"""myshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path,include,re_path

from django.conf import settings 
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static 

from django.views.static import serve

from django.utils.translation import gettext_lazy as _



urlpatterns = [
    path('admin/', admin.site.urls),
    # path('basic/',include('apps.basic.urls')),
    # path('goods/',include('apps.goods.urls')),
    # path('users/',include('apps.users.urls')),
    # path('order/',include('apps.order.urls')),
]# + staticfiles_urlpatterns()+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


if not settings.DEBUG:
    # urlpatterns += [path('^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    # path('^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT})]

    urlpatterns += [re_path('media/(?P<path>.*)', serve, {'document_root': settings.MEDIA_ROOT}),
re_path('static/(?P<path>.*)', serve, {'document_root': settings.STATIC_ROOT}),]

# 添加i18n URL配置
# urlpatterns += [
#     path(_('^i18n/'), include('django.conf.urls.i18n')),
# ]