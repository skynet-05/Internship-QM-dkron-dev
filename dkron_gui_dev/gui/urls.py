from django.urls import path
from . import views 

urlpatterns =[
    path('',views.index,name="index"),
    path('index',views.index,name="index"),
    path('schedule',views.schedule,name="schedule"),
    path('status',views.status,name="status"),
]
