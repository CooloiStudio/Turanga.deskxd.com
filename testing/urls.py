from django.conf.urls import include, url
from testing import views

urlpatterns = [
    url(r'^$', views.IndexViews.as_view(), name='index'),

    url(r'^success', views.SuccessViews.as_view(), name='success'),

    url(r'^sendmessage', views.sendmessage, name='sendmessage'),

    url(r'^beta', views.BetaViews.as_view(), name='beta'),
]