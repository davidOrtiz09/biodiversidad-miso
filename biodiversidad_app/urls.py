from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.Index.as_view(), name='index'),
    # url(r'^login/$', views.login_view, name='login'),
    url(r'^login$', views.Login.as_view(), name='login'),
    url(r'^logout$', views.Logout.as_view(), name='logout'),
    url(r'^especie/(\d+)/$', views.specie_view, name='verEspecie'),
    url(r'^addUser/$', views.add_user_view, name='addUser'),
]
