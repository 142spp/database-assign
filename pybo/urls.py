from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,                       name='index'),
    path('table_product/', views.table_product, name='table_product'),
    path('table_pc/', views.table_pc,           name='table_pc'),
    path('table_laptop/',views.table_laptop,    name='table_laptop'),
    path('table_printer/',views.table_printer,  name='table_printer'),
    path('table_query_01/',views.table_query_01, name='table_query_01'),
    path('table_query_02/',views.table_query_02, name='table_query_02'),
    path('table_query_03/',views.table_query_03, name='table_query_03'),
    path('table_query_04/',views.table_query_04, name='table_query_04'),
]