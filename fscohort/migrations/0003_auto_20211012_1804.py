# Generated by Django 3.2.8 on 2021-10-12 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fscohort', '0002_auto_20211012_1752'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ['number'], 'verbose_name_plural': 'Student_List'},
        ),
        migrations.AddField(
            model_name='student',
            name='about_student',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]
