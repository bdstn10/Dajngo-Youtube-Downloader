from django.urls import path 
from . import views 

urlpatterns = [ 
    path('youtube', views.home.as_view(), name='youtube'), 
]