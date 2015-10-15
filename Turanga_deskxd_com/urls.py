from django.conf.urls import include, url
# from django.contrib import admin

urlpatterns = [
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include('home.urls', namespace="home")),
    url(r'^download', include('download.urls', namespace="download")),
    url(r'^about', include('about.urls', namespace="about")),
]
