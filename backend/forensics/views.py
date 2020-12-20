from abc import ABC
from collections import defaultdict

from django.db.models import Avg, Count, Sum
from django.db.models.functions import TruncMonth, TruncDay
from rest_framework.response import Response
from datetime import datetime, timedelta

from .mixins import ChartMixin
from .serializers import CaseSerializer, ServiceRequestsSerializer, EvidenceSerializer
from .models import Case, Request, Evidence
# Create your views here.
from rest_framework.views import APIView


class GetCasesByDateView(APIView):
    def get(self, request, **kwargs):
        start_date_value = request.GET.get('start_date', None)
        end_date_value = request.GET.get('end_date', None)

        if start_date_value and end_date_value:
            start_date = datetime.strptime(start_date_value, '%m/%d/%Y')
            end_date = datetime.strptime(end_date_value, '%m/%d/%Y')
            total_days = end_date - start_date

            cases = Case.objects.filter(open_date__gt=start_date,
                                        open_date__lt=end_date)
        else:
            cases = Case.objects.all()
            total_days = cases.order_by('open_date').first().open_date - cases.order_by('open_date').last().open_date
        serializer = CaseSerializer(cases, many=True)

        response = {
            'data': serializer.data,
            'period_total': len(cases),
            'yesterday_total': len(cases.filter(open_date=datetime.now() - timedelta(1))),
            'daily_average': round(len(cases) / int(total_days.days))
        }

        return Response(response)


class GetServiceRequestsByDateView(APIView):

    def get(self, request, **kwargs):
        start_date_value = request.GET.get('start_date', None)
        end_date_value = request.GET.get('end_date', None)

        if start_date_value and end_date_value:
            start_date = datetime.strptime(start_date_value, '%m/%d/%Y')
            end_date = datetime.strptime(end_date_value, '%m/%d/%Y')
            total_days = end_date - start_date

            service_requests = Request.objects.filter(request_date__gte=start_date,
                                                      request_date__lte=end_date)
        else:
            service_requests = Request.objects.all()
            total_days = service_requests.order_by('request_date').first().request_date - service_requests.order_by(
                'request_date').last().request_date

        serializer = ServiceRequestsSerializer(service_requests, many=True)

        response = {
            'data': serializer.data,
            'period_total': len(service_requests),
            'yesterday_total': len(service_requests.filter(request_date=datetime.now() - timedelta(1))),
            'daily_average': round(len(service_requests) / int(total_days.days))
        }

        return Response(response)


class GetEvidenceByDateView(APIView):

    def get(self, request, **kwargs):
        start_date_value = request.GET.get('start_date', None)
        end_date_value = request.GET.get('end_date', None)

        if start_date_value and end_date_value:
            start_date = datetime.strptime(start_date_value, '%m/%d/%Y')
            end_date = datetime.strptime(end_date_value, '%m/%d/%Y')
            total_days = end_date - start_date

            evidence = Evidence.objects.filter(key_in_date__gte=start_date,
                                               key_in_date__lte=end_date)
        else:
            evidence = Evidence.objects.all()
            total_days = evidence.order_by('key_in_date').first().key_in_date - evidence.order_by(
                'key_in_date').last().key_in_date

        serializer = EvidenceSerializer(evidence, many=True)

        response = {
            'data': serializer.data,
            'period_total': len(evidence),
            'yesterday_total': len(evidence.filter(key_in_date=datetime.now() - timedelta(1))),
            'daily_average': round(len(evidence) / int(total_days.days))
        }

        return Response(response)


class GetBacklogByUnitView(APIView, ChartMixin):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.serialized_data = None
        self.start_date = None
        self.end_date = None

    def get(self, request, **kwargs):
        start_date_value = request.GET.get('start_date', None)
        end_date_value = request.GET.get('end_date', None)

        if start_date_value and end_date_value:
            self.start_date = datetime.strptime(start_date_value, '%m/%d/%Y')
            self.end_date = datetime.strptime(end_date_value, '%m/%d/%Y')

            service_requests = Request.objects.filter(request_date__gte=self.start_date,
                                                      request_date__lte=self.end_date)
        else:
            service_requests = Request.objects.all()
            self.start_date = service_requests.order_by('request_date').first().request_date
            self.end_date = service_requests.order_by('request_date').last().request_date
        serializer = ServiceRequestsSerializer(service_requests, many=True)
        self.serialized_data = serializer.data
        response = {
            'data': self.get_chart()
        }

        return Response(response)

    def get_chart(self):
        chart_data = defaultdict(lambda: defaultdict(list))
        date_counts = defaultdict(lambda: defaultdict(int))

        for result in self.serialized_data:
            try:
                dept = result['lab_dept_abbrev']
                assigned = datetime.strptime(result['assign_date'], '%m/%d/%Y')
                request = datetime.strptime(result['request_date'], '%m/%d/%Y')
                if assigned is None:
                    assigned = self.end_date + timedelta(days=1)

                in_backlog = assigned - request
                for day in range(in_backlog.days):
                    day = request + timedelta(days=day)
                    date_counts[dept][day] += 1
            except:
                continue
        for unit in date_counts:

            chart_data[unit]['name'] = unit
            items = list(date_counts[unit].items())
            items.sort()
            for backlog_date, count in items:
                chart_data[unit]['x'].append(self.chart_date(backlog_date))
                chart_data[unit]['y'].append(count)
        return [v for v in chart_data.values()]


class GetCaseloadByUnit(APIView, ChartMixin):

    def get(self, request, **kwargs):
        pass