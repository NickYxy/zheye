from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.current_time, name='current_time'),
]


