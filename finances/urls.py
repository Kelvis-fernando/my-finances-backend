from django.urls import path
from .views import WageView, WageDetailsView, SpendingView, SpendingDetailsView, MetricsPerMonthView

urlpatterns = [
    path('spendings/', SpendingView.as_view()),
    path('spendings/<int:pk>/', SpendingDetailsView.as_view()),
    path('wage/', WageView.as_view()),
    path('wage/<int:pk>/', WageDetailsView.as_view()),
    path('metrics/', MetricsPerMonthView.as_view()),
]
