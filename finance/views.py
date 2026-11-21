from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework import generics
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Wallet, Transaction
from .serializers import WalletSerializer, TransactionSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

class WalletListCreateView(generics.ListCreateAPIView):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer


class WalletDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer


class TransactionListCreateView(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

class TransactionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

