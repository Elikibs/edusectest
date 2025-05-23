# Generated by Django 5.1 on 2025-01-23 08:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academic', '0003_allocatedsubject_delete_subjectallocation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classroom',
            name='grade_level',
        ),
        migrations.RemoveField(
            model_name='student',
            name='grade_level',
        ),
        migrations.AddField(
            model_name='classlevel',
            name='grade_level',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='academic.gradelevel'),
        ),
        migrations.AddField(
            model_name='student',
            name='class_level',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='academic.classlevel'),
        ),
    ]
