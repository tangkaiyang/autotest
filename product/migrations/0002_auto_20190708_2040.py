# Generated by Django 2.2.2 on 2019-07-08 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.IntegerField(max_length=11, primary_key=True, serialize=False, verbose_name='产品编号'),
        ),
    ]
