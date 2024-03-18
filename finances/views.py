from django.shortcuts import render
from .models import Wage, Spending
from .serializers import WageSerializer
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
            return Response(serializer.data)
        
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
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SpendingView(APIView):
    def get(self, request):
        spendings = Spending.objects.all()
        serializer = WageSerializer(spendings, many=True)
        return Response(serializer.data)
        