# Generated by Django 3.0.2 on 2020-02-03 16:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Organization', '0003_jobs_fields'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jobs',
            old_name='From',
            new_name='by',
        ),
    ]
