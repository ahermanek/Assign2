from django.conf.urls import url
from . import views
from django.urls import path, re_path

app_name = 'crm'
urlpatterns = [
    path('', views.home, name='home'),
    re_path(r'^home/$', views.home, name='home'),
    path('customer_list', views.customer_list, name='customer_list'),
    path('customer/<int:pk>/edit/', views.customer_edit, name='customer_edit'),
    path('customer/<int:pk>/delete/', views.customer_delete, name='customer_delete'),
    path('service_list', views.service_list, name='service_list'),
    path('service/create/', views.service_new, name='service_new'),
    path('service/<int:pk>/edit/', views.service_edit, name='service_edit'),
    path('service/<int:pk>/delete/', views.service_delete, name='service_delete'),
    path('products_list', views.products_list, name='products_list'),
    path('products/create/', views.products_new, name='products_new'),
    path('products/<int:pk>/edit/', views.products_edit, name='products_edit'),
    path('products/<int:pk>/delete/', views.products_delete, name='products_delete'),
    path('customer/<int:pk>/summary/', views.summary, name='summary'),
]
