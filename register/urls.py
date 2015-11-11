from django.conf.urls import include, url
from register import views

urlpatterns = [
    url(r'^$', views.IndexViews.as_view(), name='index'),
    url(r'^agreement/$', views.AgreeViews.as_view(), name='agreement'),
]