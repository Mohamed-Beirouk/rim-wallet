from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from Agency import views
from .views import *


router = routers.DefaultRouter(trailing_slash=False)
router.register('Accountdetails', views.Accounts)
router.register('Transactiondetails', views.Transactions)



app_name = 'Agency'

urlpatterns = [
    path('', include(router.urls)),
    path('user/', UserRecordView.as_view(), name='users'),
    path("GetBalance/", views.GetBalance, name="Get Balance"),
    path("AddTransaction/", views.AddTransaction, name="Add a Transaction"),
    path("TransactionsList/", views.GetTransactionsList, name="Get Transactions List"),
    
    
    #GetTransactionsListLastFive UpdateReceived
    path("GetTransactionsListLastFive/", views.GetTransactionsListLastFive, name="Get Transactions List Last Five"),
    path("login/", loginclient, name="Get Transactions List"),
    path("UpdateReceived/", views.UpdateReceived, name="Update trans case"),
]
