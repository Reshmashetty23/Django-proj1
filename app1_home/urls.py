from django.urls import path, re_path
from app1_home import views
#from catalogs import views
from django.conf.urls import include
urlpatterns = [
    re_path(r'^$',views.index, name = 'index'),
]
