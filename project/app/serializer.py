from rest_framework import fields, serializers
from . models import *

class ReactSerializer(serializers.ModelSerializer):
    class Meta:
        model = React
        fields = '__all__'
        field = ['employee', 'department']