# Generated by Django 5.0.2 on 2024-02-19 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll_no', models.IntegerField()),
                ('name', models.CharField(max_length=45)),
                ('marks', models.FloatField()),
                ('address', models.TextField()),
            ],
        ),
    ]
