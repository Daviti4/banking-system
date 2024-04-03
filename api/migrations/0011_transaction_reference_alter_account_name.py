# Generated by Django 5.0.3 on 2024-04-03 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_alter_account_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='reference',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
