"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    url(r'^superuser/', admin.site.urls),
    url(r'^account/', include('apps.api.account.urls', namespace = 'account')),
    url(r'^post/', include('apps.api.post.urls', namespace = 'post')),
    url(r'^chat/', include('apps.api.chat.urls', namespace = 'chat')),
    url(r'^review/', include('apps.api.review.urls', namespace = 'review')),
    url(r'^notification/', include('apps.api.notification.urls', namespace = 'notification')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
