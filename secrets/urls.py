from django.conf.urls import url

from . import views

app_name = 'secrets'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^create/$', views.CreateView.as_view(), name='create'),
    url(r'^created/(?P<note_id>[\w]+)$', views.CreatedView.as_view(), name='created'),
    url(r'^view/(?P<given_note_id>[\w]+)/$', views.view_note, name='note'),
    url(r'^about/$', views.AboutView.as_view(), name='about'),
    url(r'^getnote/$', views.get_note, name='getnote'),
    url(r'^stats/(?P<given_note_id>[\w]+)/$', views.get_stats, name='stats')
]