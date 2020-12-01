from django.db.models import Avg, Count, Sum
from django.db.models.functions import TruncMonth, TruncDay
from rest_framework.response import Response
from datetime import datetime, timedelta
from .serializers import CaseSerializer
from .models import Case
# Create your views here.
from rest_framework.views import APIView


class GetCasesByDateView(APIView):
    def get(self, request, **kwargs):
        start_date = datetime.strptime(request.GET.get('start_date'), '%m/%d/%Y')
        end_date = datetime.strptime(request.GET.get('end_date'), '%m/%d/%Y')

        total_days = end_date - start_date

        cases = Case.objects.filter(open_date__gt=start_date,
                                    open_date__lt=end_date)

        serializer = CaseSerializer(cases, many=True)

        response = {
            'data': serializer.data,
            'period_total': len(cases),
            'yesterday_total': len(cases.filter(open_date=datetime.now() - timedelta(1))),
            'daily_average': round(len(cases) / int(total_days.days))
        }

        return Response(response)
