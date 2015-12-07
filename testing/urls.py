from django.conf.urls import include, url
from testing import views

urlpatterns = [
    url(r'^$', views.IndexViews.as_view(), name='index'),

    url(r'^success/$', views.SuccessViews.as_view(), name='success'),

    url(r'^sendmessage/$', views.sendmessage, name='sendmessage'),

    url(r'^ios/$', views.IOSViews.as_view(), name='ios'),

    url(r'^android/$', views.ANDROIDViews.as_view(), name='android'),

    url(r'^downAD/$', views.downAD, name='downAD')
]
