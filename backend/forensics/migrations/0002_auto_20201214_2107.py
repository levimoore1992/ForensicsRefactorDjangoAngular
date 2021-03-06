# Generated by Django 3.1.3 on 2020-12-14 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forensics', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ammo',
            name='nibin_entry',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='canceledrequest',
            name='priority',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='case',
            name='dfs_iad',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='case',
            name='dfs_juvenile',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='case',
            name='dfs_permconsume',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='case',
            name='restricted',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='feuammo',
            name='nibin_entry',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='feuresultextension',
            name='nibin_lead',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='feuresultextension',
            name='nibin_result_verification',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='firearms',
            name='is_operational',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='firearms',
            name='is_safety_operational',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='firearms',
            name='loaded',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='labpersonnel',
            name='active',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='lfuresultextension',
            name='afis_hit',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='lfuresultextension',
            name='fbi_hit',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='lfuresultextension',
            name='latent_identified',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='lfuresultextension',
            name='novaris_hit',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='lfuresultextension',
            name='rafis_hit',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='osticketstats',
            name='isOverdue',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='personnelteam',
            name='active',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='request',
            name='priority',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='result',
            name='is_narcotic',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='is_temptag',
            field=models.BooleanField(null=True),
        ),
    ]
