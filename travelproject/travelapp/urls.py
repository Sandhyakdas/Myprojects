from .import views
from django.urls import path

urlpatterns = [

    #path('',views.demo,name='demo'),
    path('',views.demo,name='demo')
    #path('sub/', views.addition, name='sub'),
    #path('div/', views.addition, name='div'),
    #path('mul/', views.addition, name='mul')

]