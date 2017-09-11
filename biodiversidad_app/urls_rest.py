from django.conf.urls import url
from . import views_rest

urlpatterns = [
    url(r'^$', views_rest.index, name='rest-index'),
    url(r'^get/species$', views_rest.get_species_by_category, name='get-species'),

]
