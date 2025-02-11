# Generated by Django 5.1.5 on 2025-01-21 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients_project', '0003_alter_client_created_at_alter_client_projects'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='projects',
            field=models.ManyToManyField(blank=True, related_name='projects', to='clients_project.project'),
        ),
    ]
