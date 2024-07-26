from django.urls import path
from . import views

urlpatterns = [
   path('', views.index, name='main_index'),
   path('education/<int:pk>/', views.education_detail, name='education_detail'),
   path('mk/<int:pk>/', views.mk_detail, name='mk_detail'),
   path('join_up_form/', views.join_up_form_view, name='join_up_form'),
   path('join_up_success/', views.join_up_success_view, name='join_up_success')
]



