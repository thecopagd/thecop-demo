# Generated by Django 4.1.7 on 2023-07-09 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thecop_app', '0011_areaevent_end_districtevent_end_localevent_end_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='areaevent',
            name='end',
            field=models.DateField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='districtevent',
            name='end',
            field=models.DateField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='localevent',
            name='end',
            field=models.DateField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='nationalevent',
            name='end',
            field=models.DateField(default=None, null=True),
        ),
    ]
