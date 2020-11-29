from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView


class GetCasesByDateView(APIView):
    def get(self, request, **kwargs):
        pass