from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.dineout_list, name='dineout_list'),
]