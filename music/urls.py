from django.conf.urls import url
from . import views
app_name='music'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(),name='index'),

    url(r'^(?P<pk>[1]+)/$',views.DetailView1.as_view(),name='detail1'),

    url(r'^(?P<pk>[2]+)/$',views.DetailView2.as_view(),name='detail2')



    ]