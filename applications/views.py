from django.shortcuts import render
from rest_framework import viewsets

# Create your views here.
from applications.models import Employee
from applications.serializers import EmployeeSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
    ordering_fields = ('created',)

    def get_queryset(self):
        return self.queryset.order_by('-created')