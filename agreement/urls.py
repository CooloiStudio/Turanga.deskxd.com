from django.conf.urls import include, url
from agreement import views

urlpatterns = [

    url(r'^$', views.AgreeViews.as_view(), name='agreement'),

    url(r'^privacy/$', views.PrivacyViews.as_view(), name='privacy'),

]