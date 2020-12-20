# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.contrib.auth.models import User
from django.db import models


class DashboardAppevidencetype(models.Model):
    evidence_type = models.CharField(max_length=50)
    evidence_image = models.CharField(max_length=200, blank=True, null=True)
    evidence_group = models.CharField(max_length=30, blank=True, null=True)
    list_location = models.IntegerField(blank=True, null=True)
    app_name = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dashboard_appevidencetype'


class Caseraw(models.Model):
    case_id = models.CharField(unique=True, max_length=30)
    case_details = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dashboard_caseraw'


class Dashboard(models.Model):
    user = models.ForeignKey(User, models.DO_NOTHING, unique=True)

    class Meta:
        managed = False
        db_table = 'dashboard_dashboard'


class Dashboardpermissions(models.Model):
    user = models.ForeignKey(User, models.DO_NOTHING, unique=True)

    class Meta:
        managed = False
        db_table = 'dashboard_dashboardpermissions'


class Evidenceraw(models.Model):
    case_id = models.CharField(max_length=30)
    evidence_details = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dashboard_evidenceraw'


class Actionsperformed(models.Model):
    lims_perf_act_id = models.CharField(max_length=30, blank=True, null=True)
    lims_rep_id = models.CharField(max_length=30, blank=True, null=True)
    lims_act_id = models.CharField(max_length=30, blank=True, null=True)
    lims_req_id = models.CharField(max_length=30, blank=True, null=True)
    case_id = models.CharField(max_length=30, blank=True, null=True)
    date_started = models.DateTimeField(blank=True, null=True)
    date_completed = models.DateTimeField(blank=True, null=True)
    time_spent = models.IntegerField(blank=True, null=True)
    time_spent_hours = models.DecimalField(max_digits=20, decimal_places=7, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'warehouse_actionsperformed'


class Actiontypes(models.Model):
    lims_act_id = models.CharField(max_length=30, blank=True, null=True)
    action_description = models.CharField(max_length=100, blank=True, null=True)
    agency_id = models.CharField(max_length=30, blank=True, null=True)
    dept_id = models.CharField(max_length=30, blank=True, null=True)
    lims_service_id = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'warehouse_actiontypes'


class Agency(models.Model):
    lims_agency_id = models.CharField(unique=True, max_length=30)
    name = models.CharField(max_length=60)
    abbrev = models.CharField(max_length=7, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'warehouse_agency'


class Agencypersonnel(models.Model):
    lims_agent_id = models.CharField(unique=True, max_length=30)
    last_name = models.CharField(max_length=25)
    first_name = models.CharField(max_length=25)
    display_name = models.CharField(max_length=60)
    title = models.CharField(max_length=30)
    badge_num = models.CharField(max_length=20)
    agency_name = models.CharField(max_length=60, blank=True, null=True)
    agency_abbrev = models.CharField(max_length=7, blank=True, null=True)
    lims_agency = models.ForeignKey(Agency, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'warehouse_agencypersonnel'


class Alcohol(models.Model):
    lims_alcohol_id = models.CharField(max_length=30, blank=True, null=True)
    case_id = models.CharField(max_length=30, blank=True, null=True)
    lims_request_id = models.CharField(max_length=30, blank=True, null=True)
    lims_evidence_id = models.CharField(max_length=30, blank=True, null=True)
    result_1 = models.DecimalField(max_digits=7, decimal_places=3, blank=True, null=True)
    analysis_date_1 = models.DateTimeField(blank=True, null=True)
    upload_rep_1 = models.CharField(max_length=30, blank=True, null=True)
    result_2 = models.DecimalField(max_digits=7, decimal_places=3, blank=True, null=True)
    analysis_date_2 = models.DateTimeField(blank=True, null=True)
    upload_rep_2 = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'warehouse_alcohol'


class Ammo(models.Model):
    nibin_entry = models.BooleanField(blank=True, null=True)
    evidence = models.ForeignKey('Evidence', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'warehouse_ammo'


class Arrest(models.Model):
    ccn = models.CharField(max_length=20)
    arrest_number = models.IntegerField()
    pdid = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dob = models.DateField()
    arrest_date = models.DateTimeField()
    charge_number = models.IntegerField(blank=True, null=True)
    charge_description = models.TextField(blank=True, null=True)
    arrest_category_description = models.CharField(max_length=100, blank=True, null=True)
    arrest_location = models.CharField(max_length=280, blank=True, null=True)
    arrest_location_type = models.CharField(max_length=280, blank=True, null=True)
    arrest_location_latitude = models.CharField(max_length=280, blank=True, null=True)
    arrest_location_longitude = models.CharField(max_length=280, blank=True, null=True)
    arrest_location_district = models.CharField(max_length=280, blank=True, null=True)
    arrest_location_psa = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'warehouse_arrest'


class Blacklistmapping(models.Model):
    lims_id = models.CharField(max_length=30)
    column_name = models.CharField(max_length=50, blank=True, null=True)
    lims_name = models.CharField(max_length=50, blank=True, null=True)
    dashboard_app = models.ForeignKey('Dashboardapp', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'warehouse_blacklistmapping'


class Canceledrequest(models.Model):
    lims_request_id = models.CharField(unique=True, max_length=30)
    request_number = models.CharField(max_length=150)
    canceled_code = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=30)
    edit_date = models.DateTimeField(blank=True, null=True)
    review_date = models.DateTimeField(blank=True, null=True)
    request_date = models.DateTimeField(blank=True, null=True)
    assign_date = models.DateTimeField(blank=True, null=True)
    assign_tech_date = models.DateTimeField(blank=True, null=True)
    assign_admin_date = models.DateTimeField(blank=True, null=True)
    admin_date = models.DateTimeField(blank=True, null=True)
    report_complete_date = models.DateTimeField(blank=True, null=True)
    releasable_date = models.DateTimeField(blank=True, null=True)
    canceled_date = models.DateTimeField(blank=True, null=True)
    distributed_date = models.DateTimeField(blank=True, null=True)
    turnaround_start = models.DateTimeField(blank=True, null=True)
    turnaround_end = models.DateTimeField(blank=True, null=True)
    priority = models.BooleanField(blank=True, null=True)
    requesting_agent_id = models.CharField(max_length=30, blank=True, null=True)
    service_name = models.CharField(max_length=50, blank=True, null=True)
    lab_dept_name = models.CharField(max_length=50, blank=True, null=True)
    lab_dept_abbrev = models.CharField(max_length=30, blank=True, null=True)
    lims_priority_code = models.CharField(max_length=50, blank=True, null=True)
    assigned_personnel = models.ForeignKey('Labpersonnel', models.DO_NOTHING, blank=True, null=True)
    case = models.ForeignKey('Case', models.DO_NOTHING)
    service = models.ForeignKey('Service', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'warehouse_canceledrequest'


class Case(models.Model):
    case_id = models.CharField(unique=True, max_length=15)
    open_date = models.DateTimeField()
    note = models.TextField(blank=True, null=True)
    close_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=15)
    message = models.TextField(blank=True, null=True)
    restricted = models.NullBooleanField(blank=True, null=True)
    restricted_date = models.DateTimeField(blank=True, null=True)
    dfs_district = models.CharField(max_length=3, blank=True, null=True)
    dfs_psa = models.CharField(max_length=3, blank=True, null=True)
    dfs_juvenile = models.NullBooleanField(blank=True, null=True)
    dfs_iad = models.BooleanField(blank=True, null=True)
    dfs_mcl = models.CharField(max_length=15, blank=True, null=True)
    dfs_permconsume = models.NullBooleanField(blank=True, null=True)
    dfs_permconsdate = models.DateTimeField(blank=True, null=True)
    geographic_area = models.CharField(max_length=30, blank=True, null=True)
    division = models.CharField(max_length=30, blank=True, null=True)
    subdivision = models.CharField(max_length=30, blank=True, null=True)
    latitude = models.DecimalField(max_digits=20, decimal_places=15, blank=True, null=True)
    longitude = models.DecimalField(max_digits=20, decimal_places=15, blank=True, null=True)
    dfs_ci = models.CharField(max_length=30, blank=True, null=True)
    dfs_ci_area = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'warehouse_case'


class Caseagency(models.Model):
    lims_case_agency_id = models.CharField(unique=True, max_length=30)
    agency_case_id = models.CharField(max_length=20, blank=True, null=True)
    is_primary_agency = models.IntegerField(blank=True, null=True)
    agency = models.ForeignKey(Agency, models.DO_NOTHING)
    case = models.ForeignKey(Case, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'warehouse_caseagency'


class Caseoffense(models.Model):
    lims_case_offense_id = models.CharField(unique=True, max_length=30)
    offense_date = models.DateTimeField(blank=True, null=True)
    location = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=3, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    county = models.CharField(max_length=50, blank=True, null=True)
    zip = models.CharField(max_length=12, blank=True, null=True)
    latitude = models.DecimalField(max_digits=20, decimal_places=15, blank=True, null=True)
    longitude = models.DecimalField(max_digits=20, decimal_places=15, blank=True, null=True)
    case = models.ForeignKey(Case, models.DO_NOTHING)
    offense = models.ForeignKey('Offense', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'warehouse_caseoffense'


class Caseperson(models.Model):
    lims_person_id = models.CharField(unique=True, max_length=30, blank=True, null=True)
    case_relation = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=1000, blank=True, null=True)
    first_name = models.CharField(max_length=1000, blank=True, null=True)
    middle_name = models.CharField(max_length=1000, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    race = models.CharField(max_length=30, blank=True, null=True)
    dob = models.CharField(max_length=1000, blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    agency_id = models.CharField(max_length=30, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    case = models.ForeignKey(Case, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'warehouse_caseperson'


class Covidlightvalues(models.Model):
    schedule_seq = models.CharField(max_length=100, blank=True, null=True)
    hsn = models.CharField(max_length=100, blank=True, null=True)
    cmp_result = models.CharField(max_length=100, blank=True, null=True)
    cmp = models.CharField(max_length=100, blank=True, null=True)
    collect_date = models.CharField(max_length=100, blank=True, null=True)
    sample_type = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'warehouse_covidlightvalues'


class Covidpatient(models.Model):
    last_name = models.CharField(max_length=100, blank=True, null=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    dob = models.DateTimeField(blank=True, null=True)
    gender = models.CharField(max_length=100, blank=True, null=True)
    race = models.CharField(max_length=100, blank=True, null=True)
    ethnicity = models.CharField(max_length=100, blank=True, null=True)
    street_addr = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=200, blank=True, null=True)
    state = models.CharField(max_length=200, blank=True, null=True)
    county = models.CharField(max_length=200, blank=True, null=True)
    zip = models.CharField(max_length=200, blank=True, null=True)
    seq = models.CharField(max_length=100, blank=True, null=True)
    cmp_text = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'warehouse_covidpatient'


class Covidpositivebyweek(models.Model):
    sample_id = models.AutoField(primary_key=True)
    schedule_id = models.CharField(max_length=30, blank=True, null=True)
    schedule_seq = models.CharField(max_length=30, blank=True, null=True)
    rr_schedule_seq = models.CharField(max_length=30, blank=True, null=True)
    run_date = models.CharField(max_length=30, blank=True, null=True)
    user_nbr = models.CharField(max_length=30, blank=True, null=True)
    proc_code = models.CharField(max_length=30, blank=True, null=True)
    comp_date = models.DateTimeField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    due_date = models.DateTimeField(blank=True, null=True)
    hold_date = models.DateTimeField(blank=True, null=True)
    task_status = models.CharField(max_length=30, blank=True, null=True)
    hsn = models.CharField(max_length=50, blank=True, null=True)
    wip_status = models.CharField(max_length=30, blank=True, null=True)
    matrix = models.CharField(max_length=30, blank=True, null=True)
    matrix_desc = models.CharField(max_length=100, blank=True, null=True)
    test_performed = models.CharField(max_length=30, blank=True, null=True)
    profile_name = models.CharField(max_length=50, blank=True, null=True)
    cust_id = models.CharField(max_length=30, blank=True, null=True)
    cust_name = models.CharField(max_length=100, blank=True, null=True)
    collect_date = models.DateTimeField(blank=True, null=True)
    receive_date = models.DateTimeField(blank=True, null=True)
    patient_seq = models.CharField(max_length=30, blank=True, null=True)
    cust_sample_id = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    dob = models.DateTimeField(blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    race = models.CharField(max_length=10, blank=True, null=True)
    ethnicity = models.CharField(max_length=10, blank=True, null=True)
    cmp_text = models.CharField(max_length=100, blank=True, null=True)
    cmp = models.CharField(max_length=30, blank=True, null=True)
    reported_analyte = models.CharField(max_length=30, blank=True, null=True)
    reported_text = models.CharField(max_length=100, blank=True, null=True)
    formatted_result = models.CharField(max_length=100, blank=True, null=True)
    final_result = models.CharField(max_length=50, blank=True, null=True)
    report_date = models.DateTimeField(blank=True, null=True)
    acode = models.CharField(max_length=50, blank=True, null=True)
    acode_description = models.CharField(max_length=50, blank=True, null=True)
    order_date = models.DateTimeField(blank=True, null=True)
    cancel_code = models.CharField(max_length=30, blank=True, null=True)
    street_addr = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    county = models.CharField(max_length=100, blank=True, null=True)
    zip = models.CharField(max_length=100, blank=True, null=True)
    cust_workorder_id = models.CharField(max_length=100, blank=True, null=True)
    test_id = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'warehouse_covidpositivebyweek'


class Covidrejected(models.Model):
    sample_id = models.AutoField(primary_key=True)
    schedule_id = models.CharField(max_length=30, blank=True, null=True)
    schedule_seq = models.CharField(max_length=30, blank=True, null=True)
    rr_schedule_seq = models.CharField(max_length=30, blank=True, null=True)
    run_date = models.CharField(max_length=30, blank=True, null=True)
    user_nbr = models.CharField(max_length=30, blank=True, null=True)
    proc_code = models.CharField(max_length=30, blank=True, null=True)
    comp_date = models.DateTimeField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    due_date = models.DateTimeField(blank=True, null=True)
    hold_date = models.DateTimeField(blank=True, null=True)
    task_status = models.CharField(max_length=30, blank=True, null=True)
    hsn = models.CharField(max_length=50, blank=True, null=True)
    wip_status = models.CharField(max_length=30, blank=True, null=True)
    matrix = models.CharField(max_length=30, blank=True, null=True)
    matrix_desc = models.CharField(max_length=100, blank=True, null=True)
    test_performed = models.CharField(max_length=30, blank=True, null=True)
    profile_name = models.CharField(max_length=50, blank=True, null=True)
    cust_id = models.CharField(max_length=30, blank=True, null=True)
    cust_name = models.CharField(max_length=100, blank=True, null=True)
    receive_date = models.DateTimeField(blank=True, null=True)
    patient_seq = models.CharField(max_length=30, blank=True, null=True)
    cust_sample_id = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    dob = models.DateTimeField(blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    race = models.CharField(max_length=10, blank=True, null=True)
    ethnicity = models.CharField(max_length=10, blank=True, null=True)
    cmp_text = models.CharField(max_length=100, blank=True, null=True)
    cmp = models.CharField(max_length=30, blank=True, null=True)
    reported_analyte = models.CharField(max_length=30, blank=True, null=True)
    reported_text = models.CharField(max_length=100, blank=True, null=True)
    formatted_result = models.CharField(max_length=100, blank=True, null=True)
    collect_date = models.DateTimeField(blank=True, null=True)
    final_result = models.CharField(max_length=50, blank=True, null=True)
    report_date = models.DateTimeField(blank=True, null=True)
    acode = models.CharField(max_length=50, blank=True, null=True)
    acode_description = models.CharField(max_length=50, blank=True, null=True)
    order_date = models.DateTimeField(blank=True, null=True)
    cancel_code = models.CharField(max_length=30, blank=True, null=True)
    street_addr = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    county = models.CharField(max_length=100, blank=True, null=True)
    zip = models.CharField(max_length=100, blank=True, null=True)
    rec_desc = models.CharField(max_length=200, blank=True, null=True)
    cust_workorder_id = models.CharField(max_length=100, blank=True, null=True)
    test_id = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'warehouse_covidrejected'


class Covidsample(models.Model):
    sample_id = models.AutoField(primary_key=True)
    schedule_id = models.CharField(max_length=30, blank=True, null=True)
    schedule_seq = models.CharField(max_length=30, blank=True, null=True)
    rr_schedule_seq = models.CharField(max_length=30, blank=True, null=True)
    run_date = models.CharField(max_length=30, blank=True, null=True)
    user_nbr = models.CharField(max_length=30, blank=True, null=True)
    proc_code = models.CharField(max_length=30, blank=True, null=True)
    comp_date = models.DateTimeField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    due_date = models.DateTimeField(blank=True, null=True)
    hold_date = models.DateTimeField(blank=True, null=True)
    task_status = models.CharField(max_length=30, blank=True, null=True)
    hsn = models.CharField(max_length=50, blank=True, null=True)
    wip_status = models.CharField(max_length=30, blank=True, null=True)
    matrix = models.CharField(max_length=30, blank=True, null=True)
    matrix_desc = models.CharField(max_length=100, blank=True, null=True)
    test_performed = models.CharField(max_length=30, blank=True, null=True)
    profile_name = models.CharField(max_length=50, blank=True, null=True)
    cust_id = models.CharField(max_length=30, blank=True, null=True)
    cust_name = models.CharField(max_length=100, blank=True, null=True)
    receive_date = models.DateTimeField(blank=True, null=True)
    patient_seq = models.CharField(max_length=30, blank=True, null=True)
    cust_sample_id = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    dob = models.DateTimeField(blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    race = models.CharField(max_length=10, blank=True, null=True)
    ethnicity = models.CharField(max_length=10, blank=True, null=True)
    cmp_text = models.CharField(max_length=100, blank=True, null=True)
    cmp = models.CharField(max_length=30, blank=True, null=True)
    reported_analyte = models.CharField(max_length=30, blank=True, null=True)
    reported_text = models.CharField(max_length=100, blank=True, null=True)
    formatted_result = models.CharField(max_length=100, blank=True, null=True)
    collect_date = models.DateTimeField(blank=True, null=True)
    final_result = models.CharField(max_length=50, blank=True, null=True)
    report_date = models.DateTimeField(blank=True, null=True)
    acode = models.CharField(max_length=50, blank=True, null=True)
    acode_description = models.CharField(max_length=50, blank=True, null=True)
    order_date = models.DateTimeField(blank=True, null=True)
    cancel_code = models.CharField(max_length=30, blank=True, null=True)
    street_addr = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    county = models.CharField(max_length=100, blank=True, null=True)
    zip = models.CharField(max_length=100, blank=True, null=True)
    cust_workorder_id = models.CharField(max_length=100, blank=True, null=True)
    test_id = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'warehouse_covidsample'


class Covidtest(models.Model):
    sample_id = models.AutoField(primary_key=True)
    schedule_id = models.CharField(max_length=30, blank=True, null=True)
    schedule_seq = models.CharField(max_length=30, blank=True, null=True)
    rr_schedule_seq = models.CharField(max_length=30, blank=True, null=True)
    run_date = models.CharField(max_length=30, blank=True, null=True)
    user_nbr = models.CharField(max_length=30, blank=True, null=True)
    proc_code = models.CharField(max_length=30, blank=True, null=True)
    comp_date = models.DateTimeField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    due_date = models.DateTimeField(blank=True, null=True)
    hold_date = models.DateTimeField(blank=True, null=True)
    task_status = models.CharField(max_length=30, blank=True, null=True)
    hsn = models.CharField(max_length=50, blank=True, null=True)
    wip_status = models.CharField(max_length=30, blank=True, null=True)
    matrix = models.CharField(max_length=30, blank=True, null=True)
    matrix_desc = models.CharField(max_length=100, blank=True, null=True)
    test_performed = models.CharField(max_length=30, blank=True, null=True)
    profile_name = models.CharField(max_length=50, blank=True, null=True)
    cust_id = models.CharField(max_length=30, blank=True, null=True)
    cust_name = models.CharField(max_length=100, blank=True, null=True)
    collect_date = models.DateTimeField(blank=True, null=True)
    receive_date = models.DateTimeField(blank=True, null=True)
    patient_seq = models.CharField(max_length=30, blank=True, null=True)
    cust_sample_id = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    dob = models.DateTimeField(blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    race = models.CharField(max_length=10, blank=True, null=True)
    ethnicity = models.CharField(max_length=10, blank=True, null=True)
    cmp_text = models.CharField(max_length=100, blank=True, null=True)
    cmp = models.CharField(max_length=30, blank=True, null=True)
    reported_analyte = models.CharField(max_length=30, blank=True, null=True)
    reported_text = models.CharField(max_length=100, blank=True, null=True)
    formatted_result = models.CharField(max_length=100, blank=True, null=True)
    final_result = models.CharField(max_length=50, blank=True, null=True)
    report_date = models.DateTimeField(blank=True, null=True)
    acode = models.CharField(max_length=50, blank=True, null=True)
    acode_description = models.CharField(max_length=50, blank=True, null=True)
    order_date = models.DateTimeField(blank=True, null=True)
    cancel_code = models.CharField(max_length=30, blank=True, null=True)
    street_addr = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    county = models.CharField(max_length=100, blank=True, null=True)
    zip = models.CharField(max_length=100, blank=True, null=True)
    cust_workorder_id = models.CharField(max_length=100, blank=True, null=True)
    test_id = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'warehouse_covidtest'


class Cssurequestextension(models.Model):
    dispatch = models.DateTimeField(blank=True, null=True)
    arrival = models.DateTimeField(blank=True, null=True)
    assists = models.CharField(max_length=50, blank=True, null=True)
    leica_scanned = models.IntegerField(blank=True, null=True)
    agency_departure = models.DateTimeField(blank=True, null=True)
    scene_departure = models.DateTimeField(blank=True, null=True)
    delay_notes = models.CharField(max_length=100, blank=True, null=True)
    request = models.ForeignKey('Request', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'warehouse_cssurequestextension'


class Dashboardapp(models.Model):
    apps_id = models.AutoField(primary_key=True)
    app_name = models.CharField(unique=True, max_length=30)

    class Meta:
        managed = False
        db_table = 'warehouse_dashboardapp'


class Dfsfburequestextension(models.Model):
    case_id = models.CharField(max_length=30, blank=True, null=True)
    dfs_permconsume = models.CharField(max_length=30, blank=True, null=True)
    dfs_permconsdate = models.DateTimeField(blank=True, null=True)
    dfs_permconsrequestdate = models.DateTimeField(blank=True, null=True)
    dfs_fbu_med = models.CharField(max_length=30, blank=True, null=True)
    dfs_fbu_perk = models.CharField(max_length=30, blank=True, null=True)
    dfs_fbu_perknum = models.CharField(max_length=50, blank=True, null=True)
    request = models.ForeignKey('Request', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'warehouse_dfsfburequestextension'


class Eventlog(models.Model):
    log_event = models.CharField(max_length=120, blank=True, null=True)
    log_data = models.CharField(max_length=240, blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'warehouse_eventlog'


class Evidence(models.Model):
    lims_evidence_id = models.CharField(unique=True, max_length=30)
    evidence_number = models.TextField(blank=True, null=True)
    evidence_type = models.TextField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    key_in_date = models.DateTimeField(blank=True, null=True)
    evidence_origin = models.CharField(max_length=75, blank=True, null=True)
    geographic_area = models.CharField(max_length=30, blank=True, null=True)
    division = models.CharField(max_length=30, blank=True, null=True)
    subdivision = models.CharField(max_length=30, blank=True, null=True)
    latitude = models.DecimalField(max_digits=20, decimal_places=15, blank=True, null=True)
    longitude = models.DecimalField(max_digits=20, decimal_places=15, blank=True, null=True)
    lims_container_id = models.CharField(max_length=30, blank=True, null=True)
    lims_evid_parent_id = models.CharField(max_length=30, blank=True, null=True)
    case = models.ForeignKey(Case, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'warehouse_evidence'


class Evidencemapping(models.Model):
    lims_evidence_id = models.CharField(max_length=30)
    global_evidence = models.ForeignKey('Globalevidencetype', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'warehouse_evidencemapping'


class Evidencetransfer(models.Model):
    case_id = models.CharField(max_length=30, blank=True, null=True)
    lims_evidence_id = models.CharField(max_length=30, blank=True, null=True)
    evidence_num = models.CharField(max_length=30, blank=True, null=True)
    evidence_description = models.CharField(max_length=2000, blank=True, null=True)
    evidence_type = models.CharField(max_length=200, blank=True, null=True)
    evidence_parent_id = models.CharField(max_length=30, blank=True, null=True)
    evidence_keyin_date = models.DateTimeField(blank=True, null=True)
    container_id = models.CharField(max_length=30, blank=True, null=True)
    transfer_id = models.CharField(max_length=30, blank=True, null=True)
    start_loc_name = models.CharField(max_length=100, blank=True, null=True)
    receive_loc_name = models.CharField(max_length=100, blank=True, null=True)
    transfer_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'warehouse_evidencetransfer'


class Fbuevidenceextension(models.Model):
    ndis_upload_date = models.DateTimeField(blank=True, null=True)
    sdis_upload_date = models.DateTimeField(blank=True, null=True)
    ndis_hit_date = models.DateTimeField(blank=True, null=True)
    sdis_hit_date = models.DateTimeField(blank=True, null=True)
    ndis_hit_type = models.CharField(max_length=50, blank=True, null=True)
    sdis_hit_type = models.CharField(max_length=50, blank=True, null=True)
    ndis_upload_date1 = models.DateTimeField(blank=True, null=True)
    sdis_upload_date1 = models.DateTimeField(blank=True, null=True)
    ndis_hit_date2 = models.DateTimeField(blank=True, null=True)
    sdis_hit_date2 = models.DateTimeField(blank=True, null=True)
    ndis_hit_type2 = models.CharField(max_length=50, blank=True, null=True)
    sdis_hit_type2 = models.CharField(max_length=50, blank=True, null=True)
    ndis_upload_date2 = models.DateTimeField(blank=True, null=True)
    sdis_upload_date2 = models.DateTimeField(blank=True, null=True)
    ndis_hit_date3 = models.DateTimeField(blank=True, null=True)
    sdis_hit_date3 = models.DateTimeField(blank=True, null=True)
    ndis_hit_type3 = models.CharField(max_length=50, blank=True, null=True)
    sdis_hit_type3 = models.CharField(max_length=50, blank=True, null=True)
    ndis_hit_date4 = models.DateTimeField(blank=True, null=True)
    sdis_hit_date4 = models.DateTimeField(blank=True, null=True)
    ndis_hit_type4 = models.CharField(max_length=50, blank=True, null=True)
    sdis_hit_type4 = models.CharField(max_length=50, blank=True, null=True)
    ndis_hit_date5 = models.DateTimeField(blank=True, null=True)
    sdis_hit_date5 = models.DateTimeField(blank=True, null=True)
    ndis_hit_type5 = models.CharField(max_length=50, blank=True, null=True)
    sdis_hit_type5 = models.CharField(max_length=50, blank=True, null=True)
    evidence = models.ForeignKey(Evidence, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'warehouse_fbuevidenceextension'


class Feuammo(models.Model):
    nibin_entry = models.BooleanField(blank=True, null=True)
    evidence = models.ForeignKey(Evidence, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'warehouse_feuammo'


class Feuresultextension(models.Model):
    nibin_lead = models.BooleanField(blank=True, null=True)
    nibin_result_verification = models.BooleanField(blank=True, null=True)
    nibin_hit_count = models.IntegerField(blank=True, null=True)
    result = models.ForeignKey('Result', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'warehouse_feuresultextension'


class Firearms(models.Model):
    lims_firearms_id = models.CharField(max_length=30, blank=True, null=True)
    evidence_number = models.CharField(max_length=30, blank=True, null=True)
    barrel_len = models.CharField(max_length=30, blank=True, null=True)
    barrel_cond = models.CharField(max_length=50, blank=True, null=True)
    caliber = models.CharField(max_length=30, blank=True, null=True)
    choke = models.CharField(max_length=30, blank=True, null=True)
    trigger_pull_da = models.CharField(max_length=30, blank=True, null=True)
    twist_degree = models.CharField(max_length=30, blank=True, null=True)
    twist_direction = models.CharField(max_length=30, blank=True, null=True)
    ejector = models.CharField(max_length=40, blank=True, null=True)
    extractor = models.CharField(max_length=40, blank=True, null=True)
    finish = models.CharField(max_length=40, blank=True, null=True)
    firing_pin = models.CharField(max_length=40, blank=True, null=True)
    groove_width = models.CharField(max_length=40, blank=True, null=True)
    gun_action = models.CharField(max_length=40, blank=True, null=True)
    capacity = models.CharField(max_length=30, blank=True, null=True)
    loaded = models.BooleanField(blank=True, null=True)
    manufacturer = models.CharField(max_length=40, blank=True, null=True)
    gun_model = models.CharField(max_length=40, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    is_operational = models.BooleanField(blank=True, null=True)
    serial_num = models.CharField(max_length=60, blank=True, null=True)
    gun_type = models.CharField(max_length=40, blank=True, null=True)
    land_width = models.CharField(max_length=40, blank=True, null=True)
    land_num = models.IntegerField(blank=True, null=True)
    live_round_num = models.IntegerField(blank=True, null=True)
    spent_round_num = models.IntegerField(blank=True, null=True)
    is_safety_operational = models.BooleanField(blank=True, null=True)
    safety_type = models.CharField(max_length=40, blank=True, null=True)
    trigger_pull = models.CharField(max_length=40, blank=True, null=True)
    grip_type = models.CharField(max_length=40, blank=True, null=True)
    case = models.ForeignKey(Case, models.DO_NOTHING, blank=True, null=True)
    evidence = models.ForeignKey(Evidence, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'warehouse_firearms'


class Forensicunit(models.Model):
    unit_id = models.AutoField(primary_key=True)
    abbrev = models.CharField(max_length=30)
    lims_lab_department = models.ForeignKey('Labdepartment', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'warehouse_forensicunit'


class Foresightservicemapping(models.Model):
    column_name = models.CharField(max_length=50, blank=True, null=True)
    lims_name = models.CharField(max_length=50, blank=True, null=True)
    fservice = models.ForeignKey('Foresightservices', models.DO_NOTHING)
    lims_service = models.ForeignKey('Service', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'warehouse_foresightservicemapping'


class Foresightservices(models.Model):
    fservice_id = models.AutoField(primary_key=True)
    foresight_name = models.CharField(max_length=50)
    column_name = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'warehouse_foresightservices'


class Globalevidencetype(models.Model):
    evidence_id = models.AutoField(primary_key=True)
    evidence_name = models.CharField(max_length=75, blank=True, null=True)
    evidence_group = models.CharField(max_length=75, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'warehouse_globalevidencetype'


class Labdepartment(models.Model):
    lims_lab_department_id = models.CharField(unique=True, max_length=30)
    name = models.CharField(max_length=50)
    abbrev = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'warehouse_labdepartment'


class Labpersonnel(models.Model):
    lims_rep_id = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    display_name = models.CharField(max_length=62)
    active = models.BooleanField(blank=True, null=True)
    dashboard_user = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'warehouse_labpersonnel'


class Latentserviceextension(models.Model):
    total_impressions = models.IntegerField(blank=True, null=True)
    request = models.ForeignKey('Request', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'warehouse_latentserviceextension'


class Lfuresultextension(models.Model):
    afis_entry = models.DateTimeField(blank=True, null=True)
    fbi_entry = models.DateTimeField(blank=True, null=True)
    novaris_entry = models.DateTimeField(blank=True, null=True)
    rafis_entry = models.DateTimeField(blank=True, null=True)
    afis_hit = models.BooleanField(blank=True, null=True)
    fbi_hit = models.BooleanField(blank=True, null=True)
    novaris_hit = models.BooleanField(blank=True, null=True)
    rafis_hit = models.BooleanField(blank=True, null=True)
    latent_identified = models.BooleanField(blank=True, null=True)
    true_name = models.CharField(max_length=30, blank=True, null=True)
    agency_id = models.CharField(max_length=30, blank=True, null=True)
    result = models.ForeignKey('Result', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'warehouse_lfuresultextension'


class Location(models.Model):
    location_id = models.AutoField(primary_key=True)
    case_id = models.CharField(max_length=15, blank=True, null=True)
    geographic_area = models.CharField(max_length=30, blank=True, null=True)
    division = models.CharField(max_length=30, blank=True, null=True)
    subdivision = models.CharField(max_length=30, blank=True, null=True)
    latitude = models.DecimalField(max_digits=20, decimal_places=15, blank=True, null=True)
    longitude = models.DecimalField(max_digits=20, decimal_places=15, blank=True, null=True)
    related_lims_id = models.CharField(max_length=30, blank=True, null=True)
    location_type = models.CharField(max_length=120, blank=True, null=True)
    full_address = models.CharField(max_length=250, blank=True, null=True)
    address = models.CharField(max_length=120, blank=True, null=True)
    city = models.CharField(max_length=30, blank=True, null=True)
    state = models.CharField(max_length=30, blank=True, null=True)
    zip = models.CharField(max_length=30, blank=True, null=True)
    description = models.CharField(max_length=120, blank=True, null=True)
    related_model = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'warehouse_location'


class Narcoticidentification(models.Model):
    case_id = models.CharField(max_length=30, blank=True, null=True)
    lims_result_id = models.CharField(max_length=30, blank=True, null=True)
    lims_evidence_id = models.CharField(max_length=30, blank=True, null=True)
    lims_request_id = models.CharField(max_length=30, blank=True, null=True)
    narcotic_class = models.CharField(max_length=50, blank=True, null=True)
    narcotic_substance = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'warehouse_narcoticidentification'


class Offense(models.Model):
    code = models.CharField(unique=True, max_length=30)
    description = models.CharField(max_length=100)
    category = models.CharField(max_length=75, blank=True, null=True)
    ccn = models.CharField(max_length=120, blank=True, null=True)
    charge_number = models.CharField(max_length=120, blank=True, null=True)
    offense_date = models.DateTimeField(blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    location_type = models.CharField(max_length=50, blank=True, null=True)
    latitude = models.DecimalField(max_digits=20, decimal_places=15, blank=True, null=True)
    longitude = models.DecimalField(max_digits=20, decimal_places=15, blank=True, null=True)
    location_psa = models.CharField(max_length=120, blank=True, null=True)
    location_district = models.CharField(max_length=120, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'warehouse_offense'


class Offensemapping(models.Model):
    lims_offense_id = models.CharField(max_length=30)
    offense_category = models.CharField(max_length=30)
    offense_category_description = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'warehouse_offensemapping'


class Osticketstats(models.Model):
    ticket_id = models.IntegerField()
    status = models.CharField(max_length=30, blank=True, null=True)
    state = models.CharField(max_length=30, blank=True, null=True)
    staff_assigned = models.CharField(max_length=50, blank=True, null=True)
    isoverdue = models.BooleanField(db_column='isOverdue', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(blank=True, null=True)
    closed_date = models.DateTimeField(blank=True, null=True)
    response_date = models.DateTimeField(blank=True, null=True)
    topic = models.CharField(max_length=100, blank=True, null=True)
    department = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'warehouse_osticketstats'


class Personnelteam(models.Model):
    lims_rep_id = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    display_name = models.CharField(max_length=62)
    active = models.BooleanField(blank=True, null=True)
    dash_user = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    team = models.ForeignKey('Team', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'warehouse_personnelteam'


class Phlsample(models.Model):
    sample_id = models.AutoField(primary_key=True)
    schedule_id = models.CharField(max_length=30, blank=True, null=True)
    schedule_seq = models.CharField(max_length=30, blank=True, null=True)
    user_nbr = models.CharField(max_length=30, blank=True, null=True)
    proc_code = models.CharField(max_length=30, blank=True, null=True)
    comp_date = models.DateTimeField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    due_date = models.DateTimeField(blank=True, null=True)
    hold_date = models.DateTimeField(blank=True, null=True)
    task_status = models.CharField(max_length=30, blank=True, null=True)
    hsn = models.CharField(max_length=50, blank=True, null=True)
    wip_status = models.CharField(max_length=30, blank=True, null=True)
    profile_name = models.CharField(max_length=50, blank=True, null=True)
    cust_id = models.CharField(max_length=30, blank=True, null=True)
    scollect_date = models.DateTimeField(blank=True, null=True)
    receive_date = models.DateTimeField(blank=True, null=True)
    patient_seq = models.CharField(max_length=30, blank=True, null=True)
    cust_sample_id = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    dob = models.DateTimeField(blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    cmp_text = models.CharField(max_length=100, blank=True, null=True)
    cmp = models.CharField(max_length=30, blank=True, null=True)
    reported_analyte = models.CharField(max_length=30, blank=True, null=True)
    reported_text = models.CharField(max_length=100, blank=True, null=True)
    collect_date = models.DateTimeField(blank=True, null=True)
    final_result = models.CharField(max_length=50, blank=True, null=True)
    report_date = models.DateTimeField(blank=True, null=True)
    acode = models.CharField(max_length=50, blank=True, null=True)
    acode_description = models.CharField(max_length=50, blank=True, null=True)
    order_date = models.DateTimeField(blank=True, null=True)
    cancel_code = models.CharField(max_length=30, blank=True, null=True)
    formatted_result = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'warehouse_phlsample'


class Porterleeforesight(models.Model):
    fsight_name = models.CharField(max_length=50)
    year = models.IntegerField(blank=True, null=True)
    month = models.IntegerField(blank=True, null=True)
    case_count = models.IntegerField(blank=True, null=True)
    item_count = models.IntegerField(blank=True, null=True)
    items_outsourced = models.IntegerField(blank=True, null=True)
    items_internal = models.IntegerField(blank=True, null=True)
    samples_internal = models.IntegerField(blank=True, null=True)
    sample_exams = models.IntegerField(blank=True, null=True)
    report_count = models.IntegerField(blank=True, null=True)
    median_tat_first_submission = models.IntegerField(db_column='median_TAT_first_submission', blank=True, null=True)  # Field name made lowercase.
    median_tat_last_submissino = models.IntegerField(db_column='median_TAT_last_submissino', blank=True, null=True)  # Field name made lowercase.
    open_cases_end_year = models.IntegerField(blank=True, null=True)
    open_cases_older_30days = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'warehouse_porterleeforesight'


class Property(models.Model):
    ccn = models.CharField(max_length=120)
    property_item_id = models.IntegerField()
    property_item_type = models.CharField(max_length=120)
    property_item_description = models.CharField(max_length=120)
    property_item_category = models.CharField(max_length=120)
    property_status = models.CharField(max_length=120)
    property_recovery_date = models.DateTimeField(blank=True, null=True)
    offense = models.ForeignKey(Offense, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'warehouse_property'


class Request(models.Model):
    lims_request_id = models.CharField(unique=True, max_length=30)
    request_number = models.CharField(max_length=150)
    canceled_code = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=30)
    edit_date = models.DateTimeField(blank=True, null=True)
    review_date = models.DateTimeField(blank=True, null=True)
    request_date = models.DateTimeField(blank=True, null=True)
    assign_date = models.DateTimeField(blank=True, null=True)
    assign_tech_date = models.DateTimeField(blank=True, null=True)
    assign_admin_date = models.DateTimeField(blank=True, null=True)
    admin_date = models.DateTimeField(blank=True, null=True)
    report_complete_date = models.DateTimeField(blank=True, null=True)
    releasable_date = models.DateTimeField(blank=True, null=True)
    canceled_date = models.DateTimeField(blank=True, null=True)
    distributed_date = models.DateTimeField(blank=True, null=True)
    turnaround_start = models.DateTimeField(blank=True, null=True)
    turnaround_end = models.DateTimeField(blank=True, null=True)
    priority = models.BooleanField(blank=True, null=True)
    requesting_agent_id = models.CharField(max_length=30, blank=True, null=True)
    service_name = models.CharField(max_length=50, blank=True, null=True)
    lab_dept_name = models.CharField(max_length=50, blank=True, null=True)
    lab_dept_abbrev = models.CharField(max_length=30, blank=True, null=True)
    due_date = models.DateTimeField(blank=True, null=True)
    lims_priority_code = models.CharField(max_length=50, blank=True, null=True)
    assigned_to_name = models.CharField(max_length=100, blank=True, null=True)
    reviewer_name = models.CharField(max_length=100, blank=True, null=True)
    admin_reviewer_name = models.CharField(max_length=100, blank=True, null=True)
    evidence_count = models.IntegerField(blank=True, null=True)
    admin_review_personnel = models.ForeignKey(Labpersonnel, models.DO_NOTHING, blank=True, null=True, related_name='lap_personnel')
    assigned_personnel = models.ForeignKey(Labpersonnel, models.DO_NOTHING, blank=True, null=True,related_name='assigned_personnel')
    case = models.ForeignKey(Case, models.DO_NOTHING)
    reviewer_personnel = models.ForeignKey(Labpersonnel, models.DO_NOTHING, blank=True, null=True, related_name='reviewer_personnel')
    service = models.ForeignKey('Service', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'warehouse_request'


class Requestcaseoffense(models.Model):
    canceled_request = models.ForeignKey(Canceledrequest, models.DO_NOTHING, blank=True, null=True)
    case_offense = models.ForeignKey(Caseoffense, models.DO_NOTHING)
    request = models.ForeignKey(Request, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'warehouse_requestcaseoffense'


class Requestevidence(models.Model):
    canceled_request = models.ForeignKey(Canceledrequest, models.DO_NOTHING, blank=True, null=True)
    evidence = models.ForeignKey(Evidence, models.DO_NOTHING)
    request = models.ForeignKey(Request, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'warehouse_requestevidence'


class Requestperson(models.Model):
    case = models.ForeignKey(Case, models.DO_NOTHING, blank=True, null=True)
    lims_person = models.ForeignKey(Caseperson, models.DO_NOTHING, blank=True, null=True)
    request = models.ForeignKey(Request, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'warehouse_requestperson'


class Result(models.Model):
    lims_result_id = models.CharField(unique=True, max_length=30)
    digital_data = models.CharField(max_length=30, blank=True, null=True)
    is_narcotic = models.BooleanField(blank=True, null=True)
    evidence = models.ForeignKey(Evidence, models.DO_NOTHING, blank=True, null=True)
    request = models.ForeignKey(Request, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'warehouse_result'


class Savedqueries(models.Model):
    query_name = models.CharField(max_length=120)
    username = models.CharField(max_length=30, blank=True, null=True)
    userid = models.IntegerField(blank=True, null=True)
    visibility = models.CharField(max_length=30, blank=True, null=True)
    chart_name = models.CharField(max_length=30, blank=True, null=True)
    query = models.CharField(max_length=2000, blank=True, null=True)
    columns = models.CharField(max_length=1000, blank=True, null=True)
    sort_description = models.CharField(max_length=1000, blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)
    report_template = models.CharField(max_length=2000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'warehouse_savedqueries'


class Service(models.Model):
    lims_service_id = models.CharField(unique=True, max_length=30)
    name = models.CharField(max_length=50)
    lab_department = models.ForeignKey(Labdepartment, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'warehouse_service'


class Stacssample(models.Model):
    sample_id = models.IntegerField()
    specimen_run_id = models.IntegerField()
    specimen_id = models.IntegerField(blank=True, null=True)
    parent_sample_id = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'warehouse_stacssample'


class Stacsspecimen(models.Model):
    specimen_id = models.IntegerField()
    lims_input_id = models.IntegerField()
    lab_case_number = models.CharField(max_length=50, blank=True, null=True)
    lab_evidence_number = models.CharField(max_length=50, blank=True, null=True)
    evidence_description = models.CharField(max_length=2000, blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    assignment_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'warehouse_stacsspecimen'


class Team(models.Model):
    team_id = models.AutoField(primary_key=True)
    team_name = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'warehouse_team'


class Toxanalytes(models.Model):
    lims_analyte_id = models.CharField(max_length=30, blank=True, null=True)
    analyte_name = models.CharField(max_length=100, blank=True, null=True)
    analyte_description = models.CharField(max_length=100, blank=True, null=True)
    analyte_group = models.CharField(max_length=100, blank=True, null=True)
    default_units = models.CharField(max_length=30, blank=True, null=True)
    default_method = models.CharField(max_length=100, blank=True, null=True)
    analyte_status = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'warehouse_toxanalytes'


class Toxconfirmation(models.Model):
    lims_tox_confkey = models.CharField(max_length=30, blank=True, null=True)
    case_id = models.CharField(max_length=30, blank=True, null=True)
    lims_request_id = models.CharField(max_length=30, blank=True, null=True)
    lims_evidence_id = models.CharField(max_length=30, blank=True, null=True)
    lims_analyte_id = models.CharField(max_length=30, blank=True, null=True)
    analyte_name = models.CharField(max_length=100, blank=True, null=True)
    analyte_description = models.CharField(max_length=100, blank=True, null=True)
    analyte_group = models.CharField(max_length=100, blank=True, null=True)
    tox_qunat = models.CharField(max_length=30, blank=True, null=True)
    tox_unit = models.CharField(max_length=30, blank=True, null=True)
    tox_confirmatio_method = models.CharField(max_length=100, blank=True, null=True)
    annotation = models.CharField(max_length=1000, blank=True, null=True)
    lims_rep_id = models.CharField(max_length=30, blank=True, null=True)
    rep_name = models.CharField(max_length=100, blank=True, null=True)
    lims_result_id = models.CharField(max_length=30, blank=True, null=True)
    completed_date = models.DateTimeField(blank=True, null=True)
    assigned_date = models.DateTimeField(blank=True, null=True)
    assigned_rep_id = models.CharField(max_length=30, blank=True, null=True)
    assigned_rep_name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'warehouse_toxconfirmation'


class Toxscreen(models.Model):
    lims_tox_screenkey = models.CharField(max_length=30, blank=True, null=True)
    case_id = models.CharField(max_length=30, blank=True, null=True)
    lims_request_id = models.CharField(max_length=30, blank=True, null=True)
    lims_evidence_id = models.CharField(max_length=30, blank=True, null=True)
    lims_std_screen_id = models.CharField(max_length=30, blank=True, null=True)
    screen_name = models.CharField(max_length=100, blank=True, null=True)
    screen_method = models.CharField(max_length=100, blank=True, null=True)
    result = models.IntegerField(blank=True, null=True)
    screen_value = models.CharField(max_length=30, blank=True, null=True)
    annotation = models.CharField(max_length=1000, blank=True, null=True)
    lims_rep_id = models.CharField(max_length=30, blank=True, null=True)
    rep_name = models.CharField(max_length=100, blank=True, null=True)
    completed_date = models.DateTimeField(blank=True, null=True)
    assigned_date = models.DateTimeField(blank=True, null=True)
    assigned_rep_id = models.CharField(max_length=30, blank=True, null=True)
    assigned_rep_name = models.CharField(max_length=100, blank=True, null=True)
    lims_result_id = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'warehouse_toxscreen'


class Vehicle(models.Model):
    vehicle_year = models.IntegerField(blank=True, null=True)
    make = models.CharField(max_length=30, blank=True, null=True)
    vehicle_model = models.CharField(max_length=30, blank=True, null=True)
    vehicle_body = models.CharField(max_length=30, blank=True, null=True)
    exterior_color = models.CharField(max_length=30, blank=True, null=True)
    interior_color = models.CharField(max_length=30, blank=True, null=True)
    plate_state = models.CharField(max_length=30, blank=True, null=True)
    license_num = models.CharField(max_length=30, blank=True, null=True)
    vin = models.CharField(max_length=30, blank=True, null=True)
    vin_location = models.CharField(max_length=30, blank=True, null=True)
    is_temptag = models.BooleanField(blank=True, null=True)
    vehicle_location = models.CharField(max_length=100, blank=True, null=True)
    recovery_address = models.CharField(max_length=100, blank=True, null=True)
    recovery_locality_position = models.CharField(max_length=30, blank=True, null=True)
    vehicle_status = models.CharField(max_length=30, blank=True, null=True)
    completed_date = models.DateTimeField(blank=True, null=True)
    out_date = models.DateTimeField(blank=True, null=True)
    notes = models.CharField(max_length=100, blank=True, null=True)
    evidence = models.ForeignKey(Evidence, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'warehouse_vehicle'

