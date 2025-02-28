# Generated by Django 5.1.4 on 2025-01-26 04:02

import regex_field.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("fighthealthinsurance", "0059_alter_denialtypes_diagnosis_regex_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="plantype",
            name="alt_name",
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name="plantype",
            name="negative_regex",
            field=regex_field.fields.RegexField(blank=True, max_length=400),
        ),
        migrations.AlterField(
            model_name="plantype",
            name="regex",
            field=regex_field.fields.RegexField(blank=True, max_length=400),
        ),
    ]
