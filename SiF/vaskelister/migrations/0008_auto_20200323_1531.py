# Generated by Django 2.2 on 2020-03-23 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vaskelister', '0007_auto_20200323_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vaskeliste',
            name='week',
            field=models.IntegerField(default=0),
        ),
    ]
