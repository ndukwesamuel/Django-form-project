# Generated by Django 3.1.13 on 2021-11-18 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mymodel',
            name='date_declared_missing',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='mymodel',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
