# Generated by Django 3.2.1 on 2021-05-08 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210508_0652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialissuecomments',
            name='submit_date',
            field=models.DateTimeField(default=None),
        ),
        migrations.AlterField(
            model_name='socialissuelikes',
            name='timestamp',
            field=models.DateTimeField(default=None),
        ),
    ]
