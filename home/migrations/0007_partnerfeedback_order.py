# Generated by Django 4.1.3 on 2022-12-05 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_partnerfeedbacktitle_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='partnerfeedback',
            name='order',
            field=models.IntegerField(default=99),
        ),
    ]
