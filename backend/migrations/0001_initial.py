# Generated by Django 3.1 on 2020-08-09 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sphere',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('radius', models.IntegerField()),
                ('color', models.CharField(max_length=6)),
            ],
        ),
    ]
