from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from .models import *

class UserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
        )
        validators = [
            UniqueTogetherValidator(
                queryset=User.objects.all(),
                fields=['username', 'email']
            )
        ]



class ShowTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "TransactionId",
            "CustomerFullName",
            "Input",
            "Output",
            "Note",
            "TransactionDate",
            "Currency",
            "Credit",
            "recu",
            "Account"
        )
        model = Transaction

class AddTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields=('__all__')

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'



     