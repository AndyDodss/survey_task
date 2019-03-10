# Generated by Django 2.1.7 on 2019-03-10 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0002_auto_20190310_1119'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ans',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=150)),
                ('survey', models.CharField(max_length=150)),
                ('done', models.BooleanField()),
                ('rate', models.CharField(max_length=1)),
            ],
        ),
        migrations.RemoveField(
            model_name='ask',
            name='rateA',
        ),
        migrations.RemoveField(
            model_name='ask',
            name='rateB',
        ),
        migrations.RemoveField(
            model_name='ask',
            name='rateC',
        ),
    ]
