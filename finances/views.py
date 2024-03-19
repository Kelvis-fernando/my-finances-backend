from django.shortcuts import render
from .models import Wage, Spending
from .serializers import WageSerializer, SpendingsSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

class WageView(APIView):
    def get(self, request):
        wage = Wage.objects.all()
        serializer = WageSerializer(wage, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = WageSerializer(data=request.data)
        
        if len(Wage.objects.all()) >= 1:
            return Response({"Error": "You can have only one Wage!"}, status=status.HTTP_400_BAD_REQUEST)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class WageDetailsView(APIView):
    def get(self, request, pk):
        try:
            wage = Wage.objects.get(pk=pk)
        except Wage.DoesNotExist:
             return Response({"Error": "Does not exist"}, status=status.HTTP_404_NOT_FOUND)
         
        serializer = WageSerializer(wage)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        try:
            wage = Wage.objects.get(pk=pk)
        except Wage.DoesNotExist:
             return Response({"Error": "Does not exist"}, status=status.HTTP_404_NOT_FOUND)
         
        serializer = WageSerializer(wage, data=request.data)
        
        if  serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SpendingView(APIView):
    def get(self, request):
        spendings = Spending.objects.all()
        serializer = SpendingsSerializer(spendings, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = SpendingsSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class SpendingDetailsView(APIView):
    def get(self, request, pk):
        try:
            spending = Spending.objects.get(pk=pk)
        except Spending.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = SpendingsSerializer(spending)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    def put(self, request, pk):
        try:
            spending = Spending.objects.get(pk=pk)
        except Spending.DoesNotExist:
            return Response({"Error": "Does not exist"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer =  SpendingsSerializer(spending, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        try:
            spending = Spending.objects.get(pk=pk)
        except Spending.DoesNotExist:
            return Response({"Error": "Does not exist"}, status=status.HTTP_404_NOT_FOUND)
        
        spending.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)