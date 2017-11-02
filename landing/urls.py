from django.conf.urls import url
from .views import index, characters


urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^characters/(?P<page>[0-9]+)/$', characters, name="characters"),
    url(r'^characters/', characters, name="single-characters"),
]
