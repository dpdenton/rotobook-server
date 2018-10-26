from rest_framework import serializers

from applications.models import Employee

class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = ('id', 'created', 'name', 'email', 'message')
