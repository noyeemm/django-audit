# Generated by Django 3.1 on 2020-09-13 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audit_management', '0005_auto_20200901_1053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fileupload',
            name='document',
            field=models.FileField(upload_to='media/%Y/%m/%d', verbose_name='ডকুমেন্ট সংযুক্তকরণঃ'),
        ),
        migrations.AlterField(
            model_name='fileupload',
            name='file_description',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='ডকুমেন্টের বর্ণনাঃ'),
        ),
    ]
