from django.urls import path
from . import views

#URL Config
urlpatterns =[
    path('', views.dashboard, name="dashboard")
]
    
