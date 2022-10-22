from rest_framework import serializers
from core.models import Activities

class ActivitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Activities
        fields = '__all__'
        #exclude = ('billable_to',) 
        