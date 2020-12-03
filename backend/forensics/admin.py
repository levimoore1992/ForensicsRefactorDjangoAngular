from django.contrib import admin
from .models import Case, Request, Service, LabPersonnel, LabDepartment, Evidence

# Register your models here.
admin.site.register(Case)
admin.site.register(Request)
admin.site.register(Service)
admin.site.register(LabPersonnel)
admin.site.register(LabDepartment)
admin.site.register(Evidence)
