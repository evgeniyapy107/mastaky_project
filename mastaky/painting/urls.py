from django.urls import path
from . import views

urlpatterns = [
   path('', views.painting_index, name='painting_index'),
   path('painting/<int:painting_id>/', views.painting_detail, name='painting_detail')
]