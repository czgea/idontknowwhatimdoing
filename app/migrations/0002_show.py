# Generated by Django 2.2.1 on 2019-05-22 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Show',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('showName', models.CharField(max_length=120)),
                ('showLocation', models.CharField(max_length=120)),
                ('showTime', models.TimeField()),
                ('showMessage', models.CharField(max_length=120)),
            ],
        ),
    ]
