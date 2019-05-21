from django.conf.urls import url
from . import views

app_name = 'infoglobo'

urlpatterns = [
    url(r'^$', views.ItemList.as_view(), name='item-list'),
]