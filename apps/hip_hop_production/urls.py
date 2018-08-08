from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^form/$', views.form, name="form"),
    url(r'^murda_beatz$', views.murda_beatz, name="murda_beatz"),
    url(r'^result/$', views.result, name="result"),
]