from rest_framework import serializers
from .models import Wage, Spending

class WageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wage
        fields = '__all__'
        
class SpendingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spending
        fields = '__all__'