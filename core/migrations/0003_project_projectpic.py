# Generated by Django 4.2.5 on 2023-09-09 04:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_project_projectdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='projectPic',
            field=models.ImageField(default=django.utils.timezone.now, upload_to=''),
            preserve_default=False,
        ),
    ]