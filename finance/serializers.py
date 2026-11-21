from rest_framework import serializers
from .models import Wallet, Transaction


class TransactionSerializer(serializers.ModelSerializer):
    type_name = serializers.CharField(read_only=True)

    class Meta:
        model = Transaction
        fields = ('id', 'amount', 'type', 'type_name', 'date')

   

class WalletSerializer(serializers.ModelSerializer):
    transactions = TransactionSerializer(many=True, read_only=True)
    balance = serializers.DecimalField(max_digits=12, decimal_places=2, read_only=True)

    class Meta:
        model = Wallet
        fields = ('id', 'name', 'balance', 'transactions')
