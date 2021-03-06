from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login$', views.Login.as_view(), name='login'),
    url(r'^logout$', views.Logout.as_view(), name='logout'),
    url(r'^especie/(\d+)/$', views.specie_view, name='verEspecie'),
    url(r'^registrar-usuario/$', views.add_user_view, name='addUser'),
    url(r'^actualizar-usuario/$', views.update_user_view, name='updateUser'),
    url(r'^comentar/(?P<species_id>\d+)/$', views.add_comment, name='addComment'),
    url(r'^mis-favoritos$', views.my_favorites_species, name='my-favorites-species'),
    url(r'^eliminar-favorito$', views.delete_favorite, name='delete-favorite')
]
