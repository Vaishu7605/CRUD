# Generated by Django 4.2.4 on 2023-08-03 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.CharField(max_length=3)),
                ('phone', models.CharField(max_length=13)),
                ('mail', models.CharField(max_length=50)),
            ],
        ),
    ]
