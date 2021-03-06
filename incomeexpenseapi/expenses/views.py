from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import ExpensesSerializer
from .models import Expense
from rest_framework import permissions
from .permissions import IsOwner


class ExpenseListAPIView(ListCreateAPIView):
    serializer_class = ExpensesSerializer
    queryset = Expense.objects.all()
    permissions_class = (permissions.IsAuthenticated,)

    # def perform_create(self, serializer):
    #     return serializer.save(owner=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)


class ExpenseDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ExpensesSerializer 
    permissions_class = (permissions.IsAuthenticated, IsOwner,)
    lookup_field = "id"

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)