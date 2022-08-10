from django.http import HttpResponse
from . import views
from django.urls import path


urlpatterns = [
    path('name/<str:you>/',views.sout),
    path('',views.html)
]
