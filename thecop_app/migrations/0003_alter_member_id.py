# Generated by Django 4.1.7 on 2023-06-02 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thecop_app', '0002_member_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='id',
            field=models.TextField(primary_key=True, serialize=False),
        ),
    ]