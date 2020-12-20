from django.contrib import admin
from .models import Case, Request, Service, Labpersonnel, Labdepartment, Evidence

# Register your models here.
admin.site.register(Case)
admin.site.register(Request)
admin.site.register(Service)
admin.site.register(Labpersonnel)
admin.site.register(Labdepartment)
admin.site.register(Evidence)
