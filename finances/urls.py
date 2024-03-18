from django.urls import path
from .views import WageView, WageDetailsView, SpendingView

urlpatterns = [
    path('spendings/', SpendingView.as_view()),
    path('wage/', WageView.as_view()),
    path('wage/<int:pk>/', WageDetailsView.as_view()),
]
