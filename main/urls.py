from django.urls import path
from .views import *


urlpatterns = [
    path('',InfoPage,name = 'infopage'),
    path('home/',HomePage,name='home'),
    path('post/<int:id>/<str:title>/',BlogPage,name='blog'),
]


handler404 = 'core.views.custom_404_view'