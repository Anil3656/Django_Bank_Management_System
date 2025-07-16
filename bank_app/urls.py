from django.urls import path 
from .import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('login/', views.login_user, name='login'),
    path('register/', views.register_user, name='register'),
    path('logout/', views.logout_user, name='logout'),
    path('customers/', views.customer_list, name='customer_list'),
    path('transfer/', views.transfer_money, name='transfer_money'),
    path('transactions/', views.transaction_history, name='transaction_history'),
    path('customer/<int:pk>/', views.customer_detail, name='customer_detail'),
    path('export-pdf/', views.export_transactions_pdf, name='export_pdf'),

    
]
