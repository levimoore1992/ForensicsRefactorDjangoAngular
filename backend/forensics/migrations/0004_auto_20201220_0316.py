# Generated by Django 2.1.4 on 2020-12-20 03:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forensics', '0003_auto_20201220_0259'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='actionsperformed',
            table='warehouse_actionsperformed',
        ),
        migrations.AlterModelTable(
            name='actiontypes',
            table='warehouse_actiontypes',
        ),
        migrations.AlterModelTable(
            name='agency',
            table='warehouse_agency',
        ),
        migrations.AlterModelTable(
            name='agencypersonnel',
            table='warehouse_agencypersonnel',
        ),
        migrations.AlterModelTable(
            name='alcohol',
            table='warehouse_alcohol',
        ),
        migrations.AlterModelTable(
            name='ammo',
            table='warehouse_ammo',
        ),
        migrations.AlterModelTable(
            name='arrest',
            table='warehouse_arrest',
        ),
        migrations.AlterModelTable(
            name='blacklistmapping',
            table='warehouse_blacklistmapping',
        ),
        migrations.AlterModelTable(
            name='canceledrequest',
            table='warehouse_canceledrequest',
        ),
        migrations.AlterModelTable(
            name='case',
            table='warehouse_case',
        ),
        migrations.AlterModelTable(
            name='caseagency',
            table='warehouse_caseagency',
        ),
        migrations.AlterModelTable(
            name='caseoffense',
            table='warehouse_caseoffense',
        ),
        migrations.AlterModelTable(
            name='caseperson',
            table='warehouse_caseperson',
        ),
        migrations.AlterModelTable(
            name='covidlightvalues',
            table='warehouse_covidlightvalues',
        ),
        migrations.AlterModelTable(
            name='covidpatient',
            table='warehouse_covidpatient',
        ),
        migrations.AlterModelTable(
            name='covidpositivebyweek',
            table='warehouse_covidpositivebyweek',
        ),
        migrations.AlterModelTable(
            name='covidrejected',
            table='warehouse_covidrejected',
        ),
        migrations.AlterModelTable(
            name='covidsample',
            table='warehouse_covidsample',
        ),
        migrations.AlterModelTable(
            name='covidtest',
            table='warehouse_covidtest',
        ),
        migrations.AlterModelTable(
            name='cssurequestextension',
            table='warehouse_cssurequestextension',
        ),
        migrations.AlterModelTable(
            name='dashboardapp',
            table='warehouse_dashboardapp',
        ),
        migrations.AlterModelTable(
            name='dfsfburequestextension',
            table='warehouse_dfsfburequestextension',
        ),
        migrations.AlterModelTable(
            name='eventlog',
            table='warehouse_eventlog',
        ),
        migrations.AlterModelTable(
            name='evidence',
            table='warehouse_evidence',
        ),
        migrations.AlterModelTable(
            name='evidencemapping',
            table='warehouse_evidencemapping',
        ),
        migrations.AlterModelTable(
            name='evidencetransfer',
            table='warehouse_evidencetransfer',
        ),
        migrations.AlterModelTable(
            name='fbuevidenceextension',
            table='warehouse_fbuevidenceextension',
        ),
        migrations.AlterModelTable(
            name='feuammo',
            table='warehouse_feuammo',
        ),
        migrations.AlterModelTable(
            name='feuresultextension',
            table='warehouse_feuresultextension',
        ),
        migrations.AlterModelTable(
            name='firearms',
            table='warehouse_firearms',
        ),
        migrations.AlterModelTable(
            name='forensicunit',
            table='warehouse_forensicunit',
        ),
        migrations.AlterModelTable(
            name='foresightservicemapping',
            table='warehouse_foresightservicemapping',
        ),
        migrations.AlterModelTable(
            name='foresightservices',
            table='warehouse_foresightservices',
        ),
        migrations.AlterModelTable(
            name='globalevidencetype',
            table='warehouse_globalevidencetype',
        ),
        migrations.AlterModelTable(
            name='labdepartment',
            table='warehouse_labdepartment',
        ),
        migrations.AlterModelTable(
            name='labpersonnel',
            table='warehouse_labpersonnel',
        ),
        migrations.AlterModelTable(
            name='latentserviceextension',
            table='warehouse_latentserviceextension',
        ),
        migrations.AlterModelTable(
            name='lfuresultextension',
            table='warehouse_lfuresultextension',
        ),
        migrations.AlterModelTable(
            name='location',
            table='warehouse_location',
        ),
        migrations.AlterModelTable(
            name='narcoticidentification',
            table='warehouse_narcoticidentification',
        ),
        migrations.AlterModelTable(
            name='offense',
            table='warehouse_offense',
        ),
        migrations.AlterModelTable(
            name='offensemapping',
            table='warehouse_offensemapping',
        ),
        migrations.AlterModelTable(
            name='osticketstats',
            table='warehouse_osticketstats',
        ),
        migrations.AlterModelTable(
            name='personnelteam',
            table='warehouse_personnelteam',
        ),
        migrations.AlterModelTable(
            name='phlsample',
            table='warehouse_phlsample',
        ),
        migrations.AlterModelTable(
            name='porterleeforesight',
            table='warehouse_porterleeforesight',
        ),
        migrations.AlterModelTable(
            name='property',
            table='warehouse_property',
        ),
        migrations.AlterModelTable(
            name='request',
            table='warehouse_request',
        ),
        migrations.AlterModelTable(
            name='requestcaseoffense',
            table='warehouse_requestcaseoffense',
        ),
        migrations.AlterModelTable(
            name='requestevidence',
            table='warehouse_requestevidence',
        ),
        migrations.AlterModelTable(
            name='requestperson',
            table='warehouse_requestperson',
        ),
        migrations.AlterModelTable(
            name='result',
            table='warehouse_result',
        ),
        migrations.AlterModelTable(
            name='savedqueries',
            table='warehouse_savedqueries',
        ),
        migrations.AlterModelTable(
            name='service',
            table='warehouse_service',
        ),
        migrations.AlterModelTable(
            name='stacssample',
            table='warehouse_stacssample',
        ),
        migrations.AlterModelTable(
            name='stacsspecimen',
            table='warehouse_stacsspecimen',
        ),
        migrations.AlterModelTable(
            name='team',
            table='warehouse_team',
        ),
        migrations.AlterModelTable(
            name='toxanalytes',
            table='warehouse_toxanalytes',
        ),
        migrations.AlterModelTable(
            name='toxconfirmation',
            table='warehouse_toxconfirmation',
        ),
        migrations.AlterModelTable(
            name='toxscreen',
            table='warehouse_toxscreen',
        ),
        migrations.AlterModelTable(
            name='vehicle',
            table='warehouse_vehicle',
        ),
    ]
