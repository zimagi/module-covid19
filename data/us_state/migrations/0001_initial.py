# Generated by Django 3.0 on 2020-08-23 07:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('environment', '0002_auto_20190520_0649'),
    ]

    operations = [
        migrations.CreateModel(
            name='USState',
            fields=[
                ('created', models.DateTimeField(editable=False, null=True)),
                ('updated', models.DateTimeField(editable=False, null=True)),
                ('id', models.CharField(editable=False, max_length=64, primary_key=True, serialize=False)),
                ('name', models.CharField(editable=False, max_length=256)),
                ('fips', models.IntegerField(null=True)),
                ('code', models.CharField(max_length=256, null=True)),
                ('environment', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='usstate_relation', to='environment.Environment')),
            ],
            options={
                'verbose_name': 'us state',
                'verbose_name_plural': 'us states',
                'db_table': 'covid19_us_state',
                'ordering': ['name'],
                'abstract': False,
                'unique_together': {('environment', 'name')},
            },
        ),
    ]
