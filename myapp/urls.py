from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('thank_you/', views.thank_you,name='thank_you')
]
