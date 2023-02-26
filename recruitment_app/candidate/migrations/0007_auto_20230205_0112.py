# Generated by Django 3.2.12 on 2023-02-05 01:12

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_countries.fields
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('candidate', '0006_alter_candidateprofile_stage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('name', models.CharField(max_length=50)),
                ('is_valid', models.BooleanField(default=True)),
            ],
            options={
                'get_latest_by': 'modified',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Visa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('name', models.CharField(max_length=100)),
                ('validity_in_years', models.IntegerField()),
                ('validity_in_months', models.IntegerField()),
                ('is_valid', models.BooleanField()),
            ],
            options={
                'get_latest_by': 'modified',
                'abstract': False,
            },
        ),
        migrations.AlterModelOptions(
            name='candidateprofile',
            options={'get_latest_by': 'modified'},
        ),
        migrations.RemoveField(
            model_name='candidateprofile',
            name='email',
        ),
        migrations.RemoveField(
            model_name='candidateprofile',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='candidateprofile',
            name='last_name',
        ),
        migrations.AddField(
            model_name='candidateprofile',
            name='created',
            field=django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='created'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='candidateprofile',
            name='modified',
            field=django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified'),
        ),
        migrations.CreateModel(
            name='CandidateDetailedProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('phone_number', models.CharField(default='111111', max_length=255)),
                ('sex', models.CharField(choices=[('male', 'MALE'), ('female', 'FEMALE'), ('not_disclosed', 'NA')], default='not_disclosed', max_length=190)),
                ('address', models.TextField(default='')),
                ('postal_code', models.CharField(default='600000', max_length=6, validators=[django.core.validators.RegexValidator('^[0-9]{6}$', 'Invalid postal code')])),
                ('current_residency_country', django_countries.fields.CountryField(default='US', max_length=2)),
                ('nationality', django_countries.fields.CountryField(default='IN', max_length=2)),
                ('resume_file', models.FileField(upload_to='candidate/resumes')),
                ('current_salary_monthly', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('current_bonus_yearly', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('expected_salary_monthly', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('notice_period_in_months', models.IntegerField(default=1)),
                ('require_visa_to_work', models.BooleanField(default=True)),
                ('current_visa_validity', models.DateField(default=datetime.date.today)),
                ('reference_one_at_work', models.TextField(blank=True, default='', null=True)),
                ('reference_two_at_work', models.TextField(blank=True, default='', null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('current_visa', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='candidate.visa')),
                ('skills', models.ManyToManyField(default='1', to='candidate.Skill')),
            ],
            options={
                'get_latest_by': 'modified',
                'abstract': False,
            },
        ),
    ]
