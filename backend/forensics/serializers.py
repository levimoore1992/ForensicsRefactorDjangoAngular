from rest_framework import serializers
from .models import Case, Request, Evidence


class CaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Case
        fields = '__all__'


class ServiceRequestsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = '__all__'


class EvidenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evidence
        fields = '__all__'
