# Generated by Django 5.0.1 on 2024-01-18 13:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('be_api_members', '0003_alter_country_options_organization_admin_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organization',
            name='admin',
        ),
    ]