from django.urls import path
from .views import WageView, SpendingView

urlpatterns = [
    path('spendings/', SpendingView.as_view()),
    path('wage/', WageView.as_view()),
]
