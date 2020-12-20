from rest_framework import routers
from django.urls import path

from .views import GetCasesByDateView, GetServiceRequestsByDateView, GetEvidenceByDateView, GetBacklogByUnitView

router = routers.DefaultRouter()

urlpatterns = router.urls

urlpatterns += [
    path('cases_all_by_date', GetCasesByDateView.as_view(), name='cases_all_by_date'),
    path('service_requests_by_date', GetServiceRequestsByDateView.as_view(), name='service_requests_by_date'),
    path('evidence_by_date', GetEvidenceByDateView.as_view(), name='evidence_by_date'),
    path('get_backlog_by_unit', GetBacklogByUnitView.as_view(), name='get_backlog_by_unit'),
    # path('get_caseload_by_unit', GetCaseloadByUnitView.as_view(), name='get_caseload_by_unit'),



]