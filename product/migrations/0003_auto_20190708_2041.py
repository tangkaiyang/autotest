# Generated by Django 2.2.2 on 2019-07-08 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20190708_2040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False, verbose_name='产品编号'),
        ),
    ]
