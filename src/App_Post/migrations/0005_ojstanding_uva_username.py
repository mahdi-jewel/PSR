# Generated by Django 3.0.8 on 2020-09-28 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Post', '0004_auto_20200928_2040'),
    ]

    operations = [
        migrations.AddField(
            model_name='ojstanding',
            name='uva_username',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
