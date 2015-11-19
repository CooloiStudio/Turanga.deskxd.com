from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include('home.urls', namespace="home")),
    url(r'^thanks/', include('thanks.urls', namespace="thanks")),
    # url(r'^about/', include('about.urls', namespace="about")),
    # url(r'^register/', include('register.urls', namespace="register")),
    url(r'^beta/', include('testing.urls', namespace="beta")),
    # url(r'^ueditor/',include('DjangoUeditor.urls')),
]
