from django.conf.urls import url
from . import views_rest

urlpatterns = [
    url(r'^$', views_rest.index, name='rest-index'),
]
