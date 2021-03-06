# Generated by Django 2.1.5 on 2019-02-22 18:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('url', models.CharField(max_length=200)),
                ('longname', models.CharField(max_length=200)),
                ('source', models.CharField(max_length=200)),
                ('shortname', models.CharField(max_length=200)),
                ('chart_html', models.FileField(upload_to='charts/')),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='DataRow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField(blank=True, null=True)),
                ('year', models.IntegerField()),
                ('indicator', models.CharField(max_length=100)),
                ('longname', models.CharField(max_length=500)),
                ('shortname', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=500)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mapminder_app.Country')),
                ('varname', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mapminder_app.Chart')),
            ],
        ),
    ]
