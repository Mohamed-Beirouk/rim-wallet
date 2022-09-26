from django.shortcuts import render, redirect
import requests
from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login, logout
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated



# Create your views here.
class UserRecordView(APIView):
    """
    API View to create or get a list of all the registered
    users. GET request returns the registered users whereas
    a POST request allows to create a new user.
    """
    permission_classes = [IsAdminUser]

    def get(self, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.create(validated_data=request.data)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            {
                "error": True,
                "error_msg": serializer.error_messages,
            },
            status=status.HTTP_400_BAD_REQUEST
        )


# Create your views here.
class Accounts(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class Transactions(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

@api_view([ 'POST'])
def GetBalance(request):
    tok=str(request.META.get('HTTP_AUTHORIZATION'))[6:]
    if len(tok)<1:
        return Response(
            {
                'message':'faut que vous connecter',
                'status': False
            },
            status.HTTP_200_OK
        )
    try:
        u = Token.objects.get(key=tok).user
        acc=Account.objects.get(user=u)
    except:
        return Response(
            {
                'message': 'client mahu 5alg',
                'status': False
            },
            status.HTTP_200_OK
        )
    
    return Response(
        {
            'status': True,
            'balance':acc.Balance
        },
        status.HTTP_200_OK
    )  

@api_view(['POST'])
def GetTransactionsList(request):
    tok=str(request.META.get('HTTP_AUTHORIZATION'))[6:]
    try:
        if len(tok)<1:
            return Response(
                {
                    'message':'faut que vous connecter',
                    'status': False
                },
                status.HTTP_200_OK
            )
    except:
        return Response(
                {
                    'message':'erreur token',
                    'status': False
                },
                status.HTTP_200_OK
            )
        
    try:
        u = Token.objects.get(key=tok).user
        acc=Account.objects.get(user=u)
    except:
        return Response(
            {
                'message': 'client mahu 5alg',
                'status': False
            },
            status.HTTP_200_OK
        )
    
    # try:
    L=Transaction.objects.filter(Account=acc)
    serializer_get= ShowTransactionSerializer(L, many=True)
    return Response({'status':status.HTTP_200_OK, 'Message':True, 'data':serializer_get.data})
    # except:
        # return Response({'status':status.HTTP_400_BAD_REQUEST, 'Message':'Check AccountId, Login, or Password'})


@api_view(['GET', 'POST'])
def AddTransaction(request):
    if request.method == 'POST':
        try:
            data = JSONParser().parse(request)
            Password=data['Password']
            Login=data['Login']
            AccountId=data['AccountId']
            Currency = data['Currency'] if data['Currency'] else 1
            Output = data['Output'] if data['Output'] else 0
            Input = data['Input'] if data['Input'] else 0
            TransactionId=data['TransactionId']
            Note=data['Note']
            CustomerFullName=data['CustomerFullName']

        except:
            return Response({'status':status.HTTP_400_BAD_REQUEST, 'Message':"Sorry! Check your parameters"})
        try:
            account = Account.objects.get(Password=Password, Login=Login, id=AccountId)
        except Account.DoesNotExist:
            return Response({'status':status.HTTP_400_BAD_REQUEST, 'Message':'Sorry! Check your AccountId, Login, Or Password'})
        account = Account.objects.get(id=AccountId)
        account_balance = account.Balance
        
        if(account_balance < Output):
            return Response({'status':status.HTTP_400_BAD_REQUEST, 'Message':"Your balance is not enough"})
        else:
            Credit = account_balance + (Input - Output) * Currency
        mydata= {
            "TransactionId": TransactionId,
            "Note": Note,
            "CustomerFullName": CustomerFullName,
            "Output": Output,
            "Input": Input,
            "Currency": Currency,
            "AccountId": AccountId,
            "Credit": Credit
        }
        serializer=AddTransactionSerializer(data=mydata)
        if serializer.is_valid():
            serializer.save()
            account.Balance=Credit
            account.save()
            return Response({'status':status.HTTP_200_OK, 'Message':'OK! your transaction added succesfully', 'data':serializer.data})
        else:
            return Response({'status':status.HTTP_400_BAD_REQUEST, 'Message':"Sorry! please check your inputs"})
    elif request.method == 'GET':
        return Response("Add a Transaction")
    
    
    
    
#-------------------------
# ce que j'ai augmentee

#------------------------

@api_view(['POST'])
def loginclient(request):
    uuu = request.data['username']
    ppp = request.data['password']
    null=None
    try:
        u=authenticate(username=uuu,password=ppp)
    except:
        return Response(
            {
                'status': False,
                'message': 'no account for this information',
                'data': null
            },
            status.HTTP_200_OK
        )
        
    try:
        client = Account.objects.get(user=u)
        login(request,u)
        try:
            token = Token.objects.get(user=client.user)
        except:
            token = Token.objects.create(user=client.user)

        return Response(
            {
                'id':client.id,
                'status': True,
                'token': str(token),
                'message':'login success',
                'data':{
                    'Balance':client.Balance,
                    'full_name':client.user.first_name+" "+client.user.last_name
                }
            },
            status.HTTP_200_OK
        )
    except:
        return Response(
            {
                'status': False,
                'message': 'no account for this information',
                'data': null
            },
            status.HTTP_200_OK
        )
 
 
