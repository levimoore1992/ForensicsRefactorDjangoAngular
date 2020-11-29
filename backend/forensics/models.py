from django.db import models
from django.contrib.auth.models import User


class EventLog(models.Model):
    log_event = models.CharField(max_length=120, null=True)
    log_data = models.CharField(max_length=240, null=True)
    created_date = models.DateTimeField(null=True)

    def __str__(self):
        return '%s' % (self.log_event)


class Case(models.Model):
    case_id = models.CharField(max_length=15, unique=True)
    open_date = models.DateTimeField()
    note = models.TextField(null=True)
    close_date = models.DateTimeField(null=True)
    status = models.CharField(max_length=15)
    message = models.TextField(null=True)
    offenses = models.ManyToManyField('Offense', through='CaseOffense')
    agencies = models.ManyToManyField('Agency', through='CaseAgency')
    restricted = models.NullBooleanField()
    restricted_date = models.DateTimeField(null=True)
    dfs_district = models.CharField(max_length=3, null=True)
    dfs_psa = models.CharField(max_length=3, null=True)
    dfs_juvenile = models.NullBooleanField()
    dfs_iad = models.NullBooleanField()
    dfs_mcl = models.CharField(max_length=15, null=True)
    dfs_permconsume = models.NullBooleanField()
    dfs_permconsdate = models.DateTimeField(null=True)
    geographic_area = models.CharField(max_length=30, null=True)
    division = models.CharField(max_length=30, null=True)
    subdivision = models.CharField(max_length=30, null=True)
    latitude = models.DecimalField(max_digits=20, decimal_places=15, null=True)
    longitude = models.DecimalField(max_digits=20, decimal_places=15, null=True)
    dfs_ci = models.CharField(max_length=30, null=True)
    dfs_ci_area = models.CharField(max_length=30, null=True)

    def __str__(self):
        return '%s' % (self.case_id)


class Location(models.Model):
    location_id = models.AutoField(db_column="location_id", primary_key=True)
    case_id = models.CharField(max_length=15, null=True)
    geographic_area = models.CharField(max_length=30, null=True)
    division = models.CharField(max_length=30, null=True)
    subdivision = models.CharField(max_length=30, null=True)
    latitude = models.DecimalField(max_digits=20, decimal_places=15, null=True)
    longitude = models.DecimalField(max_digits=20, decimal_places=15, null=True)
    related_lims_id = models.CharField(max_length=30, null=True)
    location_type = models.CharField(max_length=120, null=True)
    full_address = models.CharField(max_length=250, null=True)
    address = models.CharField(max_length=120, null=True)
    city = models.CharField(max_length=30, null=True)
    state = models.CharField(max_length=30, null=True)
    zip = models.CharField(max_length=30, null=True)
    description = models.CharField(max_length=120, null=True)
    related_model = models.CharField(max_length=100, null=True)

    def __str__(self):
        return '%s' % (self.case_id)


class Evidence(models.Model):
    case = models.ForeignKey('Case', to_field="case_id", on_delete=models.PROTECT)
    requests = models.ManyToManyField('Request', through="RequestEvidence")
    lims_evidence_id = models.CharField(unique=True, max_length=30)
    evidence_number = models.TextField(null=True)
    evidence_type = models.TextField(null=True)
    note = models.TextField(null=True)
    description = models.TextField(null=True)
    key_in_date = models.DateTimeField(null=True)
    evidence_origin = models.CharField(max_length=75, null=True)
    geographic_area = models.CharField(max_length=30, null=True)
    division = models.CharField(max_length=30, null=True)
    subdivision = models.CharField(max_length=30, null=True)
    latitude = models.DecimalField(max_digits=20, decimal_places=15, null=True)
    longitude = models.DecimalField(max_digits=20, decimal_places=15, null=True)
    lims_container_id = models.CharField(max_length=30, null=True)
    lims_evid_parent_id = models.CharField(max_length=30, null=True)


class GlobalEvidenceType(models.Model):
    evidence_id = models.AutoField(db_column="evidence_id", primary_key=True)
    evidence_name = models.CharField(max_length=75, null=True)
    evidence_group = models.CharField(max_length=75, null=True)

    def __str__(self):
        return '%s\%s' % (self.evidence_name, self.evidence_group)


class EvidenceMapping(models.Model):
    lims_evidence_id = models.CharField(max_length=30)
    global_evidence = models.ForeignKey('GlobalEvidenceType', to_field="evidence_id", on_delete=models.PROTECT)

    def __str__(self):
        return '%s - %s' % (self.lims_evidence_id, self.global_evidence)


class Request(models.Model):
    case = models.ForeignKey('Case', to_field="case_id", on_delete=models.PROTECT)
    service = models.ForeignKey('Service', to_field="lims_service_id", on_delete=models.PROTECT)
    # named evidence(s)-- plural to avoid a conflict with Request.evidence/Evidence.request
    evidences = models.ManyToManyField('Evidence', through="RequestEvidence")
    case_offenses = models.ManyToManyField('CaseOffense', through='RequestCaseOffense')
    lims_request_id = models.CharField(max_length=30, unique=True)
    request_number = models.CharField(max_length=150)
    canceled_code = models.IntegerField(null=True)
    status = models.CharField(max_length=30)
    edit_date = models.DateTimeField(null=True)
    review_date = models.DateTimeField(null=True)
    request_date = models.DateTimeField(null=True)
    assign_date = models.DateTimeField(null=True)
    assign_tech_date = models.DateTimeField(null=True)
    assign_admin_date = models.DateTimeField(null=True)
    admin_date = models.DateTimeField(null=True)
    report_complete_date = models.DateTimeField(null=True)
    releasable_date = models.DateTimeField(null=True)
    canceled_date = models.DateTimeField(null=True)
    distributed_date = models.DateTimeField(null=True)
    turnaround_start = models.DateTimeField(null=True)
    turnaround_end = models.DateTimeField(null=True)
    # reason renamed to priority
    priority = models.NullBooleanField()
    assigned_personnel = models.ForeignKey('LabPersonnel', to_field="lims_rep_id", null=True,
                                           related_name='assignedPersonnel', on_delete=models.PROTECT)
    reviewer_personnel = models.ForeignKey('LabPersonnel', to_field="lims_rep_id", null=True,
                                           related_name='reviewerPersonnel', on_delete=models.PROTECT)
    admin_review_personnel = models.ForeignKey('LabPersonnel', to_field="lims_rep_id", null=True,
                                               related_name='AdmRevPersonnel', on_delete=models.PROTECT)
    requesting_agent_id = models.CharField(max_length=30, null=True)
    # adding service name and lab department name for faster queries
    service_name = models.CharField(max_length=50, null=True)
    lab_dept_name = models.CharField(max_length=50, null=True)
    lab_dept_abbrev = models.CharField(max_length=30, null=True)
    due_date = models.DateTimeField(null=True)
    lims_priority_code = models.CharField(max_length=50, null=True)
    assigned_to_name = models.CharField(max_length=100, null=True)
    reviewer_name = models.CharField(max_length=100, null=True)
    admin_reviewer_name = models.CharField(max_length=100, null=True)
    evidence_count = models.IntegerField(null=True)

    def __str__(self):
        return '%s' % (self.lims_request_id)


class CanceledRequest(models.Model):
    case = models.ForeignKey('Case', to_field="case_id", on_delete=models.PROTECT)
    service = models.ForeignKey('Service', to_field="lims_service_id", on_delete=models.PROTECT)
    # named evidence(s)-- plural to avoid a conflix with Request.evidence/Evidence.request
    evidences = models.ManyToManyField('Evidence', through="RequestEvidence")
    case_offenses = models.ManyToManyField('CaseOffense', through='RequestCaseOffense')
    lims_request_id = models.CharField(max_length=30, unique=True)
    request_number = models.CharField(max_length=150)
    canceled_code = models.IntegerField(null=True)
    status = models.CharField(max_length=30)
    edit_date = models.DateTimeField(null=True)
    review_date = models.DateTimeField(null=True)
    request_date = models.DateTimeField(null=True)
    assign_date = models.DateTimeField(null=True)
    assign_tech_date = models.DateTimeField(null=True)
    assign_admin_date = models.DateTimeField(null=True)
    admin_date = models.DateTimeField(null=True)
    report_complete_date = models.DateTimeField(null=True)
    releasable_date = models.DateTimeField(null=True)
    canceled_date = models.DateTimeField(null=True)
    distributed_date = models.DateTimeField(null=True)
    turnaround_start = models.DateTimeField(null=True)
    turnaround_end = models.DateTimeField(null=True)
    # reason renamed to priority
    priority = models.NullBooleanField()
    assigned_personnel = models.ForeignKey('LabPersonnel', to_field="lims_rep_id", null=True, on_delete=models.PROTECT)
    requesting_agent_id = models.CharField(max_length=30, null=True)
    # adding service name and lab department name for faster queries
    service_name = models.CharField(max_length=50, null=True)
    lab_dept_name = models.CharField(max_length=50, null=True)
    lab_dept_abbrev = models.CharField(max_length=30, null=True)
    lims_priority_code = models.CharField(max_length=50, null=True)

    def __str__(self):
        return '%s' % (self.lims_request_id)


class CSSURequestExtension(models.Model):
    # arrival and dispatch left nullable because more fields will be added for cssu
    request = models.ForeignKey('Request', to_field="lims_request_id", related_name='cssuExts',
                                on_delete=models.PROTECT)
    dispatch = models.DateTimeField(null=True)
    arrival = models.DateTimeField(null=True)
    assists = models.CharField(max_length=50, null=True)
    leica_scanned = models.IntegerField(null=True)
    agency_departure = models.DateTimeField(null=True)
    scene_departure = models.DateTimeField(null=True)
    delay_notes = models.CharField(max_length=100, null=True)


class LatentServiceExtension(models.Model):
    # Latent fingerprint extensions
    request = models.ForeignKey('Request', to_field="lims_request_id", on_delete=models.PROTECT)
    total_impressions = models.IntegerField(null=True)


class RequestEvidence(models.Model):
    request = models.ForeignKey('Request', to_field="lims_request_id", related_name='reqkey', on_delete=models.PROTECT)
    evidence = models.ForeignKey('Evidence', to_field="lims_evidence_id", on_delete=models.PROTECT)
    canceled_request = models.ForeignKey('CanceledRequest', to_field="lims_request_id", related_name='canceledreqkey',
                                         null=True, on_delete=models.PROTECT)


class Service(models.Model):
    lims_service_id = models.CharField(max_length=30, unique=True)
    lab_department = models.ForeignKey('LabDepartment', to_field="lims_lab_department_id", on_delete=models.PROTECT)
    name = models.CharField(max_length=50)

    def __str__(self):
        return '%s' % (self.name)


class Agency(models.Model):
    lims_agency_id = models.CharField(max_length=30, unique=True)
    cases = models.ManyToManyField('Case', through='CaseAgency')
    name = models.CharField(max_length=60)
    abbrev = models.CharField(max_length=7, null=True)


class AgencyPersonnel(models.Model):
    lims_agent_id = models.CharField(max_length=30, unique=True)
    lims_agency = models.ForeignKey('Agency', to_field="lims_agency_id", on_delete=models.PROTECT)
    last_name = models.CharField(max_length=25)
    first_name = models.CharField(max_length=25)
    display_name = models.CharField(max_length=60)
    title = models.CharField(max_length=30)
    badge_num = models.CharField(max_length=20)
    agency_name = models.CharField(max_length=60, null=True)
    agency_abbrev = models.CharField(max_length=7, null=True)


class CaseAgency(models.Model):
    lims_case_agency_id = models.CharField(max_length=30, unique=True)
    case = models.ForeignKey('Case', to_field="case_id", on_delete=models.PROTECT)
    agency = models.ForeignKey('Agency', to_field="lims_agency_id", on_delete=models.PROTECT)
    agency_case_id = models.CharField(max_length=20, null=True)
    is_primary_agency = models.IntegerField(null=True)


class LabDepartment(models.Model):
    lims_lab_department_id = models.CharField(max_length=30, unique=True)
    name = models.CharField(max_length=50)
    abbrev = models.CharField(max_length=30)

    def __str__(self):
        return '%s' % (self.name)


class Offense(models.Model):
    code = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)
    category = models.CharField(max_length=75, null=True)
    cases = models.ManyToManyField('Case', through='CaseOffense')
    ccn = models.CharField(max_length=120, null=True)
    charge_number = models.CharField(max_length=120, null=True)
    offense_date = models.DateTimeField(null=True)
    location = models.CharField(max_length=100, null=True)
    location_type = models.CharField(max_length=50, null=True)
    latitude = models.DecimalField(max_digits=20, decimal_places=15, null=True)
    longitude = models.DecimalField(max_digits=20, decimal_places=15, null=True)
    location_psa = models.CharField(max_length=120, null=True)
    location_district = models.CharField(max_length=120, null=True)


class OffenseMapping(models.Model):
    lims_offense_id = models.CharField(max_length=30)
    offense_category = models.CharField(max_length=30)
    offense_category_description = models.CharField(max_length=50, null=True)

    def __str__(self):
        return '%s' % (self.offense_category)


class CaseOffense(models.Model):
    lims_case_offense_id = models.CharField(max_length=30, unique=True)
    case = models.ForeignKey('Case', to_field="case_id", on_delete=models.PROTECT)
    offense = models.ForeignKey('Offense', to_field="code", on_delete=models.PROTECT)
    offense_date = models.DateTimeField(null=True)
    location = models.CharField(max_length=50, null=True)
    state = models.CharField(max_length=3, null=True)
    city = models.CharField(max_length=50, null=True)
    county = models.CharField(max_length=50, null=True)
    zip = models.CharField(max_length=12, null=True)
    latitude = models.DecimalField(max_digits=20, decimal_places=15, null=True)
    longitude = models.DecimalField(max_digits=20, decimal_places=15, null=True)


class RequestCaseOffense(models.Model):
    request = models.ForeignKey('Request', to_field="lims_request_id", related_name='reqoffkey',
                                on_delete=models.PROTECT)
    case_offense = models.ForeignKey('CaseOffense', to_field="lims_case_offense_id", on_delete=models.PROTECT)
    canceled_request = models.ForeignKey('CanceledRequest', to_field="lims_request_id",
                                         related_name='canceledreqoffkey', null=True, on_delete=models.PROTECT)


class Result(models.Model):
    request = models.ForeignKey('Request', to_field='lims_request_id', null=True, on_delete=models.PROTECT)
    evidence = models.ForeignKey('Evidence', to_field='lims_evidence_id', null=True, on_delete=models.PROTECT)
    lims_result_id = models.CharField(max_length=30, unique=True)
    digital_data = models.CharField(max_length=30, null=True)
    is_narcotic = models.NullBooleanField()


class NarcoticIdentification(models.Model):
    case_id = models.CharField(max_length=30, null=True)
    lims_result_id = models.CharField(max_length=30, null=True)
    lims_evidence_id = models.CharField(max_length=30, null=True)
    lims_request_id = models.CharField(max_length=30, null=True)
    narcotic_class = models.CharField(max_length=50, null=True)
    narcotic_substance = models.CharField(max_length=50, null=True)


class LFUResultExtension(models.Model):
    result = models.ForeignKey('Result', to_field='lims_result_id', on_delete=models.PROTECT)
    afis_entry = models.DateTimeField(null=True)
    fbi_entry = models.DateTimeField(null=True)
    novaris_entry = models.DateTimeField(null=True)
    rafis_entry = models.DateTimeField(null=True)
    afis_hit = models.NullBooleanField()
    fbi_hit = models.NullBooleanField()
    novaris_hit = models.NullBooleanField()
    rafis_hit = models.NullBooleanField()
    latent_identified = models.NullBooleanField()
    true_name = models.CharField(max_length=30, null=True)
    agency_id = models.CharField(max_length=30, null=True)


class FEUResultExtension(models.Model):
    result = models.ForeignKey('Result', to_field='lims_result_id', on_delete=models.PROTECT)
    nibin_lead = models.NullBooleanField()
    nibin_result_verification = models.NullBooleanField()
    nibin_hit_count = models.IntegerField(null=True)


class FEUAmmo(models.Model):
    evidence = models.ForeignKey('Evidence', to_field='lims_evidence_id', on_delete=models.PROTECT)
    nibin_entry = models.NullBooleanField()


class Ammo(models.Model):
    evidence = models.ForeignKey('Evidence', to_field='lims_evidence_id', on_delete=models.PROTECT)
    nibin_entry = models.NullBooleanField()


class FBUEvidenceExtension(models.Model):
    evidence = models.ForeignKey('Evidence', to_field='lims_evidence_id', on_delete=models.PROTECT)
    ndis_upload_date = models.DateTimeField(null=True)
    sdis_upload_date = models.DateTimeField(null=True)
    ndis_hit_date = models.DateTimeField(null=True)
    sdis_hit_date = models.DateTimeField(null=True)

    ndis_hit_type = models.CharField(max_length=50, null=True)
    sdis_hit_type = models.CharField(max_length=50, null=True)

    ndis_upload_date1 = models.DateTimeField(null=True)
    sdis_upload_date1 = models.DateTimeField(null=True)
    ndis_hit_date2 = models.DateTimeField(null=True)
    sdis_hit_date2 = models.DateTimeField(null=True)

    ndis_hit_type2 = models.CharField(max_length=50, null=True)
    sdis_hit_type2 = models.CharField(max_length=50, null=True)

    ndis_upload_date2 = models.DateTimeField(null=True)
    sdis_upload_date2 = models.DateTimeField(null=True)
    ndis_hit_date3 = models.DateTimeField(null=True)
    sdis_hit_date3 = models.DateTimeField(null=True)

    ndis_hit_type3 = models.CharField(max_length=50, null=True)
    sdis_hit_type3 = models.CharField(max_length=50, null=True)

    ndis_hit_date4 = models.DateTimeField(null=True)
    sdis_hit_date4 = models.DateTimeField(null=True)

    ndis_hit_type4 = models.CharField(max_length=50, null=True)
    sdis_hit_type4 = models.CharField(max_length=50, null=True)

    ndis_hit_date5 = models.DateTimeField(null=True)
    sdis_hit_date5 = models.DateTimeField(null=True)

    ndis_hit_type5 = models.CharField(max_length=50, null=True)
    sdis_hit_type5 = models.CharField(max_length=50, null=True)


class DfsFbuRequestExtension(models.Model):
    request = models.ForeignKey('Request', to_field="lims_request_id", on_delete=models.PROTECT)
    case_id = models.CharField(max_length=30, null=True)
    dfs_permconsume = models.CharField(max_length=30, null=True)
    dfs_permconsdate = models.DateTimeField(null=True)
    dfs_permconsrequestdate = models.DateTimeField(null=True)
    dfs_fbu_med = models.CharField(max_length=30, null=True)
    dfs_fbu_perk = models.CharField(max_length=30, null=True)
    dfs_fbu_perknum = models.CharField(max_length=50, null=True)


class LabPersonnel(models.Model):
    lims_rep_id = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    display_name = models.CharField(max_length=62)
    active = models.BooleanField()
    dashboard_user = models.CharField(max_length=30, null=True)

    def __str__(self):
        return '%s' % (self.display_name)


class ForesightServices(models.Model):
    fservice_id = models.AutoField(db_column="fservice_id", primary_key=True)
    foresight_name = models.CharField(max_length=50)
    column_name = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=50, null=True)
    services = models.ManyToManyField('Service', through='ForesightServiceMapping', related_name='on_service')

    def __str__(self):
        return '%s' % (self.foresight_name)


class ForesightServiceMapping(models.Model):
    fservice = models.ForeignKey('ForesightServices', to_field='fservice_id', on_delete=models.PROTECT)
    lims_service = models.ForeignKey('Service', to_field='lims_service_id', null=True, on_delete=models.PROTECT)
    column_name = models.CharField(max_length=50, null=True)
    lims_name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return '%s %s' % (self.column_name, self.lims_name)


class PersonnelTeam(models.Model):
    lims_rep_id = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    display_name = models.CharField(max_length=62)
    active = models.BooleanField()
    team = models.ForeignKey('Team', to_field="team_id", null=True, blank=True, related_name='on_team',
                             on_delete=models.PROTECT)
    dash_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='on_dash_user')

    def __str__(self):
        return '%s' % (self.display_name)


class Team(models.Model):
    team_id = models.AutoField(db_column="team_id", primary_key=True)
    team_name = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)

    def __str__(self):
        return '%s' % (self.team_name)


class ForensicUnit(models.Model):
    unit_id = models.AutoField(db_column="unit_id", primary_key=True)
    abbrev = models.CharField(max_length=30)
    lims_lab_department = models.ForeignKey('LabDepartment', to_field="lims_lab_department_id", null=True, blank=True,
                                            related_name='on_unit', on_delete=models.PROTECT)

    def __str__(self):
        return '%s' % (self.abbrev)


class DashboardApp(models.Model):
    apps_id = models.AutoField(db_column="apps_id", primary_key=True)
    app_name = models.CharField(max_length=30, unique=True)

    # evidence = models.ForeignKey('Evidence', to_field="lims_evidence_id", null=True, related_name='on_evid')

    def __str__(self):
        return '%s' % (self.app_name)


class BlacklistMapping(models.Model):
    dashboard_app = models.ForeignKey('DashboardApp', to_field='app_name', related_name='app_map',
                                      on_delete=models.PROTECT)
    lims_id = models.CharField(max_length=30)
    column_name = models.CharField(max_length=50, null=True)
    lims_name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return '%s %s' % (self.column_name, self.lims_name)


class Vehicle(models.Model):
    evidence = models.ForeignKey('Evidence', to_field='lims_evidence_id', null=True, on_delete=models.PROTECT)
    vehicle_year = models.IntegerField(null=True)
    make = models.CharField(max_length=30, null=True)
    vehicle_model = models.CharField(max_length=30, null=True)
    vehicle_body = models.CharField(max_length=30, null=True)
    exterior_color = models.CharField(max_length=30, null=True)
    interior_color = models.CharField(max_length=30, null=True)
    plate_state = models.CharField(max_length=30, null=True)
    license_num = models.CharField(max_length=30, null=True)
    vin = models.CharField(max_length=30, null=True)
    vin_location = models.CharField(max_length=30, null=True)
    is_temptag = models.NullBooleanField()
    vehicle_location = models.CharField(max_length=100, null=True)
    recovery_address = models.CharField(max_length=100, null=True)
    recovery_locality_position = models.CharField(max_length=30, null=True)
    vehicle_status = models.CharField(max_length=30, null=True)
    completed_date = models.DateTimeField(null=True)
    out_date = models.DateTimeField(null=True)
    notes = models.CharField(max_length=100, null=True)

    def __str__(self):
        return '%s %s' % (self.make, self.vehicle_model)


class CasePerson(models.Model):
    case = models.ForeignKey('Case', to_field='case_id', null=True, on_delete=models.PROTECT)
    lims_person_id = models.CharField(max_length=30, unique=True, null=True)
    case_relation = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=1000, null=True)
    first_name = models.CharField(max_length=1000, null=True)
    middle_name = models.CharField(max_length=1000, null=True)
    address = models.CharField(max_length=100, null=True)
    race = models.CharField(max_length=30, null=True)
    dob = models.CharField(max_length=1000, null=True)
    gender = models.CharField(max_length=10, null=True)
    agency_id = models.CharField(max_length=30, null=True)
    age = models.IntegerField(null=True)


class RequestPerson(models.Model):
    case = models.ForeignKey('Case', to_field='case_id', null=True, on_delete=models.PROTECT)
    request = models.ForeignKey('Request', to_field='lims_request_id', null=True, on_delete=models.PROTECT)
    lims_person = models.ForeignKey('CasePerson', to_field='lims_person_id', null=True, on_delete=models.PROTECT)


# Firearms specs
class Firearms(models.Model):
    case = models.ForeignKey('Case', to_field='case_id', null=True, on_delete=models.PROTECT)
    evidence = models.ForeignKey('Evidence', to_field='lims_evidence_id', null=True, on_delete=models.PROTECT)
    lims_firearms_id = models.CharField(max_length=30, null=True)
    evidence_number = models.CharField(max_length=30, null=True)
    barrel_len = models.CharField(max_length=30, null=True)
    barrel_cond = models.CharField(max_length=50, null=True)
    caliber = models.CharField(max_length=30, null=True)
    choke = models.CharField(max_length=30, null=True)
    trigger_pull_da = models.CharField(max_length=30, null=True)
    twist_degree = models.CharField(max_length=30, null=True)
    twist_direction = models.CharField(max_length=30, null=True)
    ejector = models.CharField(max_length=40, null=True)
    extractor = models.CharField(max_length=40, null=True)
    finish = models.CharField(max_length=40, null=True)
    firing_pin = models.CharField(max_length=40, null=True)
    groove_width = models.CharField(max_length=40, null=True)
    gun_action = models.CharField(max_length=40, null=True)
    capacity = models.CharField(max_length=30, null=True)
    loaded = models.NullBooleanField()
    manufacturer = models.CharField(max_length=40, null=True)
    gun_model = models.CharField(max_length=40, null=True)
    notes = models.TextField(null=True)
    is_operational = models.NullBooleanField()
    serial_num = models.CharField(max_length=60, null=True)
    gun_type = models.CharField(max_length=40, null=True)
    land_width = models.CharField(max_length=40, null=True)
    land_num = models.IntegerField(null=True)
    live_round_num = models.IntegerField(null=True)
    spent_round_num = models.IntegerField(null=True)
    is_safety_operational = models.NullBooleanField()
    safety_type = models.CharField(max_length=40, null=True)
    trigger_pull = models.CharField(max_length=40, null=True)
    grip_type = models.CharField(max_length=40, null=True)


class SavedQueries(models.Model):
    query_name = models.CharField(max_length=120)
    username = models.CharField(max_length=30, null=True)
    userid = models.IntegerField(null=True)
    visibility = models.CharField(max_length=30, null=True)
    chart_name = models.CharField(max_length=30, null=True)
    query = models.CharField(max_length=2000, null=True)
    columns = models.CharField(max_length=1000, null=True)
    sort_description = models.CharField(max_length=1000, null=True)
    update_date = models.DateTimeField(null=True)
    report_template = models.CharField(max_length=2000, null=True)


class EvidenceTransfer(models.Model):
    case_id = models.CharField(max_length=30, null=True)
    lims_evidence_id = models.CharField(max_length=30, null=True)
    evidence_num = models.CharField(max_length=30, null=True)
    evidence_description = models.CharField(max_length=2000, null=True)
    evidence_type = models.CharField(max_length=200, null=True)
    evidence_parent_id = models.CharField(max_length=30, null=True)
    evidence_keyin_date = models.DateTimeField(null=True)
    container_id = models.CharField(max_length=30, null=True)
    transfer_id = models.CharField(max_length=30, null=True)
    start_loc_name = models.CharField(max_length=100, null=True)
    receive_loc_name = models.CharField(max_length=100, null=True)
    transfer_date = models.DateTimeField(null=True)


class ActionTypes(models.Model):
    lims_act_id = models.CharField(max_length=30, null=True)
    action_description = models.CharField(max_length=100, null=True)
    agency_id = models.CharField(max_length=30, null=True)
    dept_id = models.CharField(max_length=30, null=True)
    lims_service_id = models.CharField(max_length=30, null=True)


class ActionsPerformed(models.Model):
    lims_perf_act_id = models.CharField(max_length=30, null=True)
    lims_rep_id = models.CharField(max_length=30, null=True)
    lims_act_id = models.CharField(max_length=30, null=True)
    lims_req_id = models.CharField(max_length=30, null=True)
    case_id = models.CharField(max_length=30, null=True)
    date_started = models.DateTimeField(null=True)
    date_completed = models.DateTimeField(null=True)
    time_spent = models.IntegerField(null=True)
    time_spent_hours = models.DecimalField(max_digits=20, decimal_places=7, null=True)


# Toxicology models for LIMS and Dashboard
class ToxConfirmation(models.Model):
    lims_tox_confkey = models.CharField(max_length=30, null=True)
    case_id = models.CharField(max_length=30, null=True)
    lims_request_id = models.CharField(max_length=30, null=True)
    lims_evidence_id = models.CharField(max_length=30, null=True)
    lims_analyte_id = models.CharField(max_length=30, null=True)
    analyte_name = models.CharField(max_length=100, null=True)
    analyte_description = models.CharField(max_length=100, null=True)
    analyte_group = models.CharField(max_length=100, null=True)
    tox_qunat = models.CharField(max_length=30, null=True)
    tox_unit = models.CharField(max_length=30, null=True)
    tox_confirmatio_method = models.CharField(max_length=100, null=True)
    annotation = models.CharField(max_length=1000, null=True)
    lims_rep_id = models.CharField(max_length=30, null=True)
    rep_name = models.CharField(max_length=100, null=True)
    lims_result_id = models.CharField(max_length=30, null=True)
    completed_date = models.DateTimeField(null=True)
    assigned_date = models.DateTimeField(null=True)
    assigned_rep_id = models.CharField(max_length=30, null=True)
    assigned_rep_name = models.CharField(max_length=100, null=True)


class ToxAnalytes(models.Model):
    lims_analyte_id = models.CharField(max_length=30, null=True)
    analyte_name = models.CharField(max_length=100, null=True)
    analyte_description = models.CharField(max_length=100, null=True)
    analyte_group = models.CharField(max_length=100, null=True)
    default_units = models.CharField(max_length=30, null=True)
    default_method = models.CharField(max_length=100, null=True)
    analyte_status = models.CharField(max_length=30, null=True)


class ToxScreen(models.Model):
    lims_tox_screenkey = models.CharField(max_length=30, null=True)
    case_id = models.CharField(max_length=30, null=True)
    lims_request_id = models.CharField(max_length=30, null=True)
    lims_evidence_id = models.CharField(max_length=30, null=True)
    lims_std_screen_id = models.CharField(max_length=30, null=True)
    screen_name = models.CharField(max_length=100, null=True)
    screen_method = models.CharField(max_length=100, null=True)
    result = models.IntegerField(null=True)
    screen_value = models.CharField(max_length=30, null=True)
    annotation = models.CharField(max_length=1000, null=True)
    lims_rep_id = models.CharField(max_length=30, null=True)
    rep_name = models.CharField(max_length=100, null=True)
    completed_date = models.DateTimeField(null=True)
    assigned_date = models.DateTimeField(null=True)
    assigned_rep_id = models.CharField(max_length=30, null=True)
    assigned_rep_name = models.CharField(max_length=100, null=True)
    lims_result_id = models.CharField(max_length=30, null=True)


class Alcohol(models.Model):
    lims_alcohol_id = models.CharField(max_length=30, null=True)
    case_id = models.CharField(max_length=30, null=True)
    lims_request_id = models.CharField(max_length=30, null=True)
    lims_evidence_id = models.CharField(max_length=30, null=True)
    result_1 = models.DecimalField(max_digits=7, decimal_places=3, null=True)
    analysis_date_1 = models.DateTimeField(null=True)
    upload_rep_1 = models.CharField(max_length=30, null=True)
    result_2 = models.DecimalField(max_digits=7, decimal_places=3, null=True)
    analysis_date_2 = models.DateTimeField(null=True)
    upload_rep_2 = models.CharField(max_length=30, null=True)


# Stacs Models
class StacsSpecimen(models.Model):
    specimen_id = models.IntegerField()
    lims_input_id = models.IntegerField()
    lab_case_number = models.CharField(max_length=50, null=True)
    lab_evidence_number = models.CharField(max_length=50, null=True)
    evidence_description = models.CharField(max_length=2000, null=True)
    created_date = models.DateTimeField(null=True)
    assignment_date = models.DateTimeField(null=True)


class StacsSample(models.Model):
    sample_id = models.IntegerField()
    specimen_run_id = models.IntegerField()
    specimen_id = models.IntegerField(null=True)
    parent_sample_id = models.IntegerField(null=True)
    created_date = models.DateTimeField(null=True)


# PorterLee Models
class PorterLeeForesight(models.Model):
    fsight_name = models.CharField(max_length=50)
    year = models.IntegerField(null=True)
    month = models.IntegerField(null=True)
    case_count = models.IntegerField(null=True)
    item_count = models.IntegerField(null=True)
    items_outsourced = models.IntegerField(null=True)
    items_internal = models.IntegerField(null=True)
    samples_internal = models.IntegerField(null=True)
    sample_exams = models.IntegerField(null=True)
    report_count = models.IntegerField(null=True)
    median_TAT_first_submission = models.IntegerField(null=True)
    median_TAT_last_submissino = models.IntegerField(null=True)
    open_cases_end_year = models.IntegerField(null=True)
    open_cases_older_30days = models.IntegerField(null=True)


# OSTicket Models
class OsticketStats(models.Model):
    ticket_id = models.IntegerField()
    status = models.CharField(max_length=30, null=True)
    state = models.CharField(max_length=30, null=True)
    staff_assigned = models.CharField(max_length=50, null=True)
    isOverdue = models.NullBooleanField()
    created_date = models.DateTimeField(null=True)
    closed_date = models.DateTimeField(null=True)
    response_date = models.DateTimeField(null=True)
    topic = models.CharField(max_length=100, null=True)
    department = models.CharField(max_length=100, null=True)


# Horizon Chemware model
class PhlSample(models.Model):
    sample_id = models.AutoField(db_column="sample_id", primary_key=True)
    schedule_id = models.CharField(max_length=30, null=True)
    schedule_seq = models.CharField(max_length=30, null=True)
    user_nbr = models.CharField(max_length=30, null=True)
    proc_code = models.CharField(max_length=30, null=True)
    comp_date = models.DateTimeField(null=True)
    create_date = models.DateTimeField(null=True)
    due_date = models.DateTimeField(null=True)
    hold_date = models.DateTimeField(null=True)
    task_status = models.CharField(max_length=30, null=True)
    hsn = models.CharField(max_length=50, null=True)
    wip_status = models.CharField(max_length=30, null=True)
    profile_name = models.CharField(max_length=50, null=True)
    cust_id = models.CharField(max_length=30, null=True)
    scollect_date = models.DateTimeField(null=True)
    receive_date = models.DateTimeField(null=True)
    patient_seq = models.CharField(max_length=30, null=True)
    cust_sample_id = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=50, null=True)
    first_name = models.CharField(max_length=50, null=True)
    dob = models.DateTimeField(null=True)
    gender = models.CharField(max_length=10, null=True)
    cmp_text = models.CharField(max_length=100, null=True)
    cmp = models.CharField(max_length=30, null=True)
    reported_analyte = models.CharField(max_length=30, null=True)
    reported_text = models.CharField(max_length=100, null=True)
    collect_date = models.DateTimeField(null=True)
    final_result = models.CharField(max_length=50, null=True)
    report_date = models.DateTimeField(null=True)
    acode = models.CharField(max_length=50, null=True)
    acode_description = models.CharField(max_length=50, null=True)
    order_date = models.DateTimeField(null=True)
    cancel_code = models.CharField(max_length=30, null=True)
    formatted_result = models.CharField(max_length=100, null=True)


# Horizon Chemware model
class CovidSample(models.Model):
    sample_id = models.AutoField(db_column="sample_id", primary_key=True)
    schedule_id = models.CharField(max_length=30, null=True)
    schedule_seq = models.CharField(max_length=30, null=True)
    rr_schedule_seq = models.CharField(max_length=30, null=True)
    run_date = models.CharField(max_length=30, null=True)
    user_nbr = models.CharField(max_length=30, null=True)
    proc_code = models.CharField(max_length=30, null=True)
    comp_date = models.DateTimeField(null=True)
    create_date = models.DateTimeField(null=True)
    due_date = models.DateTimeField(null=True)
    hold_date = models.DateTimeField(null=True)
    task_status = models.CharField(max_length=30, null=True)
    hsn = models.CharField(max_length=50, null=True)
    wip_status = models.CharField(max_length=30, null=True)
    matrix = models.CharField(max_length=30, null=True)
    matrix_desc = models.CharField(max_length=100, null=True)
    test_performed = models.CharField(max_length=30, null=True)
    profile_name = models.CharField(max_length=50, null=True)
    cust_id = models.CharField(max_length=30, null=True)
    cust_name = models.CharField(max_length=100, null=True)
    receive_date = models.DateTimeField(null=True)
    patient_seq = models.CharField(max_length=30, null=True)
    cust_sample_id = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=50, null=True)
    first_name = models.CharField(max_length=50, null=True)
    dob = models.DateTimeField(null=True)
    gender = models.CharField(max_length=10, null=True)
    race = models.CharField(max_length=10, null=True)
    ethnicity = models.CharField(max_length=10, null=True)
    cmp_text = models.CharField(max_length=100, null=True)
    cmp = models.CharField(max_length=30, null=True)
    reported_analyte = models.CharField(max_length=30, null=True)
    reported_text = models.CharField(max_length=100, null=True)
    formatted_result = models.CharField(max_length=100, null=True)
    collect_date = models.DateTimeField(null=True)
    final_result = models.CharField(max_length=50, null=True)
    report_date = models.DateTimeField(null=True)
    acode = models.CharField(max_length=50, null=True)
    acode_description = models.CharField(max_length=50, null=True)
    order_date = models.DateTimeField(null=True)
    cancel_code = models.CharField(max_length=30, null=True)
    street_addr = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)
    state = models.CharField(max_length=100, null=True)
    county = models.CharField(max_length=100, null=True)
    zip = models.CharField(max_length=100, null=True)
    cust_workorder_id = models.CharField(max_length=100, null=True)
    test_id = models.CharField(max_length=100, null=True)


# Horizon Chemware model
class CovidRejected(models.Model):
    sample_id = models.AutoField(db_column="sample_id", primary_key=True)
    schedule_id = models.CharField(max_length=30, null=True)
    schedule_seq = models.CharField(max_length=30, null=True)
    rr_schedule_seq = models.CharField(max_length=30, null=True)
    run_date = models.CharField(max_length=30, null=True)
    user_nbr = models.CharField(max_length=30, null=True)
    proc_code = models.CharField(max_length=30, null=True)
    comp_date = models.DateTimeField(null=True)
    create_date = models.DateTimeField(null=True)
    due_date = models.DateTimeField(null=True)
    hold_date = models.DateTimeField(null=True)
    task_status = models.CharField(max_length=30, null=True)
    hsn = models.CharField(max_length=50, null=True)
    wip_status = models.CharField(max_length=30, null=True)
    matrix = models.CharField(max_length=30, null=True)
    matrix_desc = models.CharField(max_length=100, null=True)
    test_performed = models.CharField(max_length=30, null=True)
    profile_name = models.CharField(max_length=50, null=True)
    cust_id = models.CharField(max_length=30, null=True)
    cust_name = models.CharField(max_length=100, null=True)
    receive_date = models.DateTimeField(null=True)
    patient_seq = models.CharField(max_length=30, null=True)
    cust_sample_id = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=50, null=True)
    first_name = models.CharField(max_length=50, null=True)
    dob = models.DateTimeField(null=True)
    gender = models.CharField(max_length=10, null=True)
    race = models.CharField(max_length=10, null=True)
    ethnicity = models.CharField(max_length=10, null=True)
    cmp_text = models.CharField(max_length=100, null=True)
    cmp = models.CharField(max_length=30, null=True)
    reported_analyte = models.CharField(max_length=30, null=True)
    reported_text = models.CharField(max_length=100, null=True)
    formatted_result = models.CharField(max_length=100, null=True)
    collect_date = models.DateTimeField(null=True)
    final_result = models.CharField(max_length=50, null=True)
    report_date = models.DateTimeField(null=True)
    acode = models.CharField(max_length=50, null=True)
    acode_description = models.CharField(max_length=50, null=True)
    order_date = models.DateTimeField(null=True)
    cancel_code = models.CharField(max_length=30, null=True)
    street_addr = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)
    state = models.CharField(max_length=100, null=True)
    county = models.CharField(max_length=100, null=True)
    zip = models.CharField(max_length=100, null=True)
    rec_desc = models.CharField(max_length=200, null=True)
    cust_workorder_id = models.CharField(max_length=100, null=True)
    test_id = models.CharField(max_length=100, null=True)


# Horizon Chemware model
class CovidPatient(models.Model):
    last_name = models.CharField(max_length=100, null=True)
    first_name = models.CharField(max_length=100, null=True)
    dob = models.DateTimeField(max_length=100, null=True)
    gender = models.CharField(max_length=100, null=True)
    race = models.CharField(max_length=100, null=True)
    ethnicity = models.CharField(max_length=100, null=True)
    street_addr = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    county = models.CharField(max_length=200, null=True)
    zip = models.CharField(max_length=200, null=True)
    seq = models.CharField(max_length=100, null=True)
    cmp_text = models.CharField(max_length=200, null=True)


# Horizon Chemware model
class CovidLightValues(models.Model):
    schedule_seq = models.CharField(max_length=100, null=True)
    hsn = models.CharField(max_length=100, null=True)
    cmp_result = models.CharField(max_length=100, null=True)
    cmp = models.CharField(max_length=100, null=True)
    collect_date = models.CharField(max_length=100, null=True)
    sample_type = models.CharField(max_length=100, null=True)


# Horizon Chemware model
class CovidTest(models.Model):
    sample_id = models.AutoField(db_column="sample_id", primary_key=True)
    schedule_id = models.CharField(max_length=30, null=True)
    schedule_seq = models.CharField(max_length=30, null=True)
    rr_schedule_seq = models.CharField(max_length=30, null=True)
    run_date = models.CharField(max_length=30, null=True)
    user_nbr = models.CharField(max_length=30, null=True)
    proc_code = models.CharField(max_length=30, null=True)
    comp_date = models.DateTimeField(null=True)
    create_date = models.DateTimeField(null=True)
    due_date = models.DateTimeField(null=True)
    hold_date = models.DateTimeField(null=True)
    task_status = models.CharField(max_length=30, null=True)
    hsn = models.CharField(max_length=50, null=True)
    wip_status = models.CharField(max_length=30, null=True)
    matrix = models.CharField(max_length=30, null=True)
    matrix_desc = models.CharField(max_length=100, null=True)
    test_performed = models.CharField(max_length=30, null=True)
    profile_name = models.CharField(max_length=50, null=True)
    cust_id = models.CharField(max_length=30, null=True)
    cust_name = models.CharField(max_length=100, null=True)
    collect_date = models.DateTimeField(null=True)
    receive_date = models.DateTimeField(null=True)
    patient_seq = models.CharField(max_length=30, null=True)
    cust_sample_id = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=50, null=True)
    first_name = models.CharField(max_length=50, null=True)
    dob = models.DateTimeField(null=True)
    gender = models.CharField(max_length=10, null=True)
    race = models.CharField(max_length=10, null=True)
    ethnicity = models.CharField(max_length=10, null=True)
    cmp_text = models.CharField(max_length=100, null=True)
    cmp = models.CharField(max_length=30, null=True)
    reported_analyte = models.CharField(max_length=30, null=True)
    reported_text = models.CharField(max_length=100, null=True)
    formatted_result = models.CharField(max_length=100, null=True)
    final_result = models.CharField(max_length=50, null=True)
    report_date = models.DateTimeField(null=True)
    acode = models.CharField(max_length=50, null=True)
    acode_description = models.CharField(max_length=50, null=True)
    order_date = models.DateTimeField(null=True)
    cancel_code = models.CharField(max_length=30, null=True)
    street_addr = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)
    state = models.CharField(max_length=100, null=True)
    county = models.CharField(max_length=100, null=True)
    zip = models.CharField(max_length=100, null=True)
    cust_workorder_id = models.CharField(max_length=100, null=True)
    test_id = models.CharField(max_length=100, null=True)


# Horizon Chemware model
class CovidPositiveByWeek(models.Model):
    sample_id = models.AutoField(db_column="sample_id", primary_key=True)
    schedule_id = models.CharField(max_length=30, null=True)
    schedule_seq = models.CharField(max_length=30, null=True)
    rr_schedule_seq = models.CharField(max_length=30, null=True)
    run_date = models.CharField(max_length=30, null=True)
    user_nbr = models.CharField(max_length=30, null=True)
    proc_code = models.CharField(max_length=30, null=True)
    comp_date = models.DateTimeField(null=True)
    create_date = models.DateTimeField(null=True)
    due_date = models.DateTimeField(null=True)
    hold_date = models.DateTimeField(null=True)
    task_status = models.CharField(max_length=30, null=True)
    hsn = models.CharField(max_length=50, null=True)
    wip_status = models.CharField(max_length=30, null=True)
    matrix = models.CharField(max_length=30, null=True)
    matrix_desc = models.CharField(max_length=100, null=True)
    test_performed = models.CharField(max_length=30, null=True)
    profile_name = models.CharField(max_length=50, null=True)
    cust_id = models.CharField(max_length=30, null=True)
    cust_name = models.CharField(max_length=100, null=True)
    collect_date = models.DateTimeField(null=True)
    receive_date = models.DateTimeField(null=True)
    patient_seq = models.CharField(max_length=30, null=True)
    cust_sample_id = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=50, null=True)
    first_name = models.CharField(max_length=50, null=True)
    dob = models.DateTimeField(null=True)
    gender = models.CharField(max_length=10, null=True)
    race = models.CharField(max_length=10, null=True)
    ethnicity = models.CharField(max_length=10, null=True)
    cmp_text = models.CharField(max_length=100, null=True)
    cmp = models.CharField(max_length=30, null=True)
    reported_analyte = models.CharField(max_length=30, null=True)
    reported_text = models.CharField(max_length=100, null=True)
    formatted_result = models.CharField(max_length=100, null=True)
    final_result = models.CharField(max_length=50, null=True)
    report_date = models.DateTimeField(null=True)
    acode = models.CharField(max_length=50, null=True)
    acode_description = models.CharField(max_length=50, null=True)
    order_date = models.DateTimeField(null=True)
    cancel_code = models.CharField(max_length=30, null=True)
    street_addr = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)
    state = models.CharField(max_length=100, null=True)
    county = models.CharField(max_length=100, null=True)
    zip = models.CharField(max_length=100, null=True)
    cust_workorder_id = models.CharField(max_length=100, null=True)
    test_id = models.CharField(max_length=100, null=True)


class Arrest(models.Model):
    ccn = models.CharField(max_length=20)
    arrest_number = models.IntegerField()
    pdid = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dob = models.DateField()
    arrest_date = models.DateTimeField()
    charge_number = models.IntegerField(null=True, blank=True)
    charge_description = models.TextField(null=True, blank=True)
    arrest_category_description = models.CharField(max_length=100, null=True, blank=True)
    arrest_location = models.CharField(max_length=280, null=True, blank=True)
    arrest_location_type = models.CharField(max_length=280, null=True, blank=True)
    arrest_location_latitude = models.CharField(max_length=280, null=True, blank=True)
    arrest_location_longitude = models.CharField(max_length=280, null=True, blank=True)
    arrest_location_district = models.CharField(max_length=280, null=True, blank=True)
    arrest_location_psa = models.IntegerField(null=True, blank=True)

    @property
    def full_name(self):
        return '%s %s'.format(self.first_name, self.last_name)


class Property(models.Model):
    ccn = models.CharField(max_length=120)
    offense = models.ForeignKey(Offense, on_delete=models.PROTECT, null=True)
    property_item_id = models.IntegerField()
    property_item_type = models.CharField(max_length=120)
    property_item_description = models.CharField(max_length=120)
    property_item_category = models.CharField(max_length=120)
    property_status = models.CharField(max_length=120)
    property_recovery_date = models.DateTimeField(null=True)
