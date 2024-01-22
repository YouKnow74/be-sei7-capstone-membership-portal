# Generated by Django 5.0.1 on 2024-01-22 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('be_api_members', '0003_alter_profile_organization'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='status',
            field=models.CharField(choices=[('A', 'Active'), ('NA', 'Not Active'), ('IC', 'Incomplete')], default='IC'),
        ),
    ]