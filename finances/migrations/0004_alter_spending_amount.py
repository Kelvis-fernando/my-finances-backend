# Generated by Django 5.0.3 on 2024-03-19 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finances', '0003_alter_wage_wage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spending',
            name='amount',
            field=models.FloatField(),
        ),
    ]
