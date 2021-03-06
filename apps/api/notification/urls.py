from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^list/$', views.NotificationListAPIView.as_view(), name='notification-list'),
    url(r'^(?P<id>[0-9a-f-]+)/read/$', views.UpdateNotificationAPIView.as_view(), name='update-notification'),
]
