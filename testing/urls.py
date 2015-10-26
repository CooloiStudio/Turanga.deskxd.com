from django.conf.urls import include, url
from testing import views

urlpatterns = [
    url(r'^$', views.IndexViews.as_view(), name='index'),
]