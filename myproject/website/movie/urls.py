from django.conf.urls import url
from . import views
urlpatterns=[
	url(r'^(?P<pk>[0-9]+)/$',views.detail,name="detail"),
	url(r'^list/$',views.list.as_view(),name="list"),
	url(r'^$',views.movie,name='movie'),
]
