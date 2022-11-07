# Generated by Django 3.2.12 on 2022-11-05 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidate', '0004_alter_candidateprofile_stage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidateprofile',
            name='stage',
            field=models.CharField(choices=[('pending', 'PENDING'), ('reviewing', 'REVIEWING'), ('shortlisted', 'SHORTLISTED'), ('interviewing', 'INTERVIEWING'), ('advanced_interviewing', 'ADVANCED INTERVIEWING'), ('rejected_by_company', 'REJECTED BY COMPANY'), ('offered', 'OFFERED'), ('hired', 'HIRED'), ('rejected_by_candidate', 'REJECTED BY CANDIDATE'), ('on_hold', 'ON HOLD')], default='pending', max_length=150),
        ),
    ]