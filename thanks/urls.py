from django.conf.urls import include, url
from thanks import views

urlpatterns = [
    url(r'^$', views.IndexViews.as_view(), name='index'),

    # url(r'^version/$', views.get_version, name='version'),

    url(r'^pubdate/$', views.get_time, name='pubdate'),
]