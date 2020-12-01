from rest_framework import routers
from django.urls import path

from  .views import GetCasesByDateView

router = routers.DefaultRouter()

urlpatterns = router.urls

urlpatterns += [
    path('cases_all_by_date', GetCasesByDateView.as_view(), name='cases_all_by_date')
]