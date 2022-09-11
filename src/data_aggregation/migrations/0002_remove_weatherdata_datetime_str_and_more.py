# Generated by Django 4.1.1 on 2022-09-08 19:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data_aggregation', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='weatherdata',
            name='datetime_str',
        ),
        migrations.RemoveField(
            model_name='weatherdata',
            name='max_temp',
        ),
        migrations.AddField(
            model_name='weatherdata',
            name='country',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='data_aggregation.country'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='weatherdata',
            name='datetimeStr',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='weatherdata',
            name='maxt',
            field=models.DecimalField(decimal_places=2, max_digits=255, null=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='lat',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=255, null=True, verbose_name='Geographical coordinates latitude'),
        ),
        migrations.AlterField(
            model_name='country',
            name='lon',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=255, null=True, verbose_name='Geographical coordinates longitude)'),
        ),
        migrations.AlterField(
            model_name='weatherdata',
            name='cloudcover',
            field=models.DecimalField(decimal_places=2, max_digits=255, null=True),
        ),
        migrations.AlterField(
            model_name='weatherdata',
            name='conditions',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='weatherdata',
            name='datetime',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='weatherdata',
            name='dew',
            field=models.DecimalField(decimal_places=2, max_digits=255, null=True),
        ),
        migrations.AlterField(
            model_name='weatherdata',
            name='humidity',
            field=models.DecimalField(decimal_places=2, max_digits=255, null=True),
        ),
        migrations.AlterField(
            model_name='weatherdata',
            name='mint',
            field=models.DecimalField(decimal_places=2, max_digits=255, null=True),
        ),
        migrations.AlterField(
            model_name='weatherdata',
            name='precip',
            field=models.DecimalField(decimal_places=2, max_digits=255, null=True),
        ),
        migrations.AlterField(
            model_name='weatherdata',
            name='precipcover',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='weatherdata',
            name='sealevelpressure',
            field=models.DecimalField(decimal_places=2, max_digits=255, null=True),
        ),
        migrations.AlterField(
            model_name='weatherdata',
            name='snow',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='weatherdata',
            name='solarenergy',
            field=models.DecimalField(decimal_places=2, max_digits=255, null=True),
        ),
        migrations.AlterField(
            model_name='weatherdata',
            name='visibility',
            field=models.DecimalField(decimal_places=2, max_digits=255, null=True),
        ),
        migrations.AlterField(
            model_name='weatherdata',
            name='wdir',
            field=models.DecimalField(decimal_places=2, max_digits=255, null=True),
        ),
        migrations.AlterField(
            model_name='weatherdata',
            name='wgust',
            field=models.DecimalField(decimal_places=2, max_digits=255, null=True),
        ),
        migrations.AlterField(
            model_name='weatherdata',
            name='wspd',
            field=models.DecimalField(decimal_places=2, max_digits=255, null=True),
        ),
    ]
