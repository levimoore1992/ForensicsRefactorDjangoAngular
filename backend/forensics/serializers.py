from rest_framework import serializers
from .models import Case, Request, Evidence


class CaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Case
        fields = [
            'case_id',
            'close_date'
        ]


class ServiceRequestsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = [
            'request_number',
            'request_date',
            'assign_date',
            'lab_dept_abbrev'
        ]


class EvidenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evidence
        fields = [
            'key_in_date',
            'evidence_number'
        ]
