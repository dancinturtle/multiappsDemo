from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="secretIndex"),
    url(r'^register$', views.register, name="secretreg"),
    url(r'^login$', views.login),
    url(r'^process$', views.process),
    url(r'^like/(?P<id>\d+)/(?P<sentby>\w+)$', views.newlike),
    url(r'^delete/(?P<id>\d+)/(?P<sentby>\w+)$', views.delete),
    url(r'^secrets$', views.secrets, name="showSecrets"),
    url(r'^popular$', views.popular),

    url(r'^logout$', views.logout),


]
