# Generated by Django 4.1.3 on 2022-12-05 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_maintechnologycard_order_portifolio_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='partnerfeedbacktitle',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]