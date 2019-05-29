from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
#plan col-auto mx-2 my-2 justify-content-center favorite rectangle_block1