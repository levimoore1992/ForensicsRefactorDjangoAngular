# Generated by Django 2.1.4 on 2020-12-20 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forensics', '0002_auto_20201214_2107'),
    ]

    operations = [
        migrations.CreateModel(
            name='Caseraw',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('case_id', models.CharField(max_length=30, unique=True)),
                ('case_details', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'dashboard_caseraw',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Dashboard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'dashboard_dashboard',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DashboardAppevidencetype',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('evidence_type', models.CharField(max_length=50)),
                ('evidence_image', models.CharField(blank=True, max_length=200, null=True)),
                ('evidence_group', models.CharField(blank=True, max_length=30, null=True)),
                ('list_location', models.IntegerField(blank=True, null=True)),
                ('app_name', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'db_table': 'dashboard_appevidencetype',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Dashboardpermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'dashboard_dashboardpermissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Evidenceraw',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('case_id', models.CharField(max_length=30)),
                ('evidence_details', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'dashboard_evidenceraw',
                'managed': False,
            },
        ),
        migrations.AlterModelOptions(
            name='actionsperformed',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='actiontypes',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='agency',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='agencypersonnel',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='alcohol',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='ammo',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='arrest',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='blacklistmapping',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='canceledrequest',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='case',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='caseagency',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='caseoffense',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='caseperson',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='covidlightvalues',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='covidpatient',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='covidpositivebyweek',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='covidrejected',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='covidsample',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='covidtest',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='cssurequestextension',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='dashboardapp',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='dfsfburequestextension',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='eventlog',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='evidence',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='evidencemapping',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='evidencetransfer',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='fbuevidenceextension',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='feuammo',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='feuresultextension',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='firearms',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='forensicunit',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='foresightservicemapping',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='foresightservices',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='globalevidencetype',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='labdepartment',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='labpersonnel',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='latentserviceextension',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='lfuresultextension',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='location',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='narcoticidentification',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='offense',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='offensemapping',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='osticketstats',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='personnelteam',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='phlsample',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='porterleeforesight',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='property',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='request',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='requestcaseoffense',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='requestevidence',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='requestperson',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='result',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='savedqueries',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='service',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='stacssample',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='stacsspecimen',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='team',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='toxanalytes',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='toxconfirmation',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='toxscreen',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='vehicle',
            options={'managed': False},
        ),
    ]
