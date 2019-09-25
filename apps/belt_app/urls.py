from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^/new$', views.new),
    url(r'^/new/add$', views.add_job),
    url(r'^/(?P<jobID>\d+)/show$', views.show),
    url(r'^/(?P<jobID>\d+)/edit$', views.edit),
    url(r'^/(?P<jobID>\d+)/edit/update$', views.process_edit),
    url(r'^/(?P<jobID>\d+)/delete$', views.delete),
    url(r'^/(?P<jobID>\d+)/delete2$', views.delete2),
    url(r'^/(?P<jobID>\d+)/join$', views.join),
    url(r'^/(?P<jobID>\d+)/giveup$', views.giveup),

]
