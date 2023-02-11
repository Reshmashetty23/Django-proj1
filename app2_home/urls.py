from django.urls import path, re_path
from app2_home import views
#from catalogs import views
urlpatterns = [
    re_path(r'^$',views.mainWindow, name = 'mainWindow'),
]