from django.urls import path
from django.conf.urls import url
from . import views
from django.conf.urls import include

app_name = 'NeoNoteApp'


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^home$', views.index, name='index'),

    url(r'^signup/$', views.sign_up, name='sign_up'),
    url(r'^login/$', views.user_login, name='user_login'),
    url(r'^logout/$', views.user_logout, name='user_logout'),

    url(r'^profile/$', views.view_profile, name='view_profile'),

    url(r'^places/$', views.view_places, name='view_places'),

    url(r'^add_place/$', views.new_place, name='new_place'),

    url(r'^about/$', views.view_about, name='view_about'),


]
