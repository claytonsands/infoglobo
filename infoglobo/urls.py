from django.conf.urls import url
from . import views
from rest_framework_mongoengine import routers as merouters


app_name = 'infoglobo'
merouter = merouters.DefaultRouter()
merouter.register(r'mongo', views.ItemList)

urlpatterns = [
    #url(r'^$', views.ItemList.as_view(), name='item-list'),
]

urlpatterns += merouter.urls