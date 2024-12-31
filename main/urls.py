from django.urls import path
from .views import *


urlpatterns = [
    path('',HomePage,name='home'),
    path('location/', user_location_view, name='user_location'),
    path('post/<int:id>/<str:title>/',BlogPage,name='blog'),

    
]