from django.urls import path
from . import views

urlpatterns= [

        path('id/<str:id>', views.idfetch),

        ]

