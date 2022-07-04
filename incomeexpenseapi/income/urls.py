from django.urls import path
from . import views
from .views import IncomeDetailAPIView,IncomeListAPIView

urlpatterns = [
    path('', views.IncomeListAPIView.as_view(), name="incomes"),
    path('<int:id>', views.IncomeDetailAPIView.as_view(), name="income"),
]