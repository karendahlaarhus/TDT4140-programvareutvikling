# Generated by Django 3.0.3 on 2020-02-20 12:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('studentby', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='kollektiv',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kollektivNr', models.IntegerField()),
                ('studentby', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studentby.studentby')),
            ],
        ),
    ]