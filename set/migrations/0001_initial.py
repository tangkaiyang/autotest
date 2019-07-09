# Generated by Django 2.2.2 on 2019-07-09 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Set',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('setname', models.CharField(max_length=64, verbose_name='系统名称')),
                ('setvalue', models.CharField(max_length=20, verbose_name='系统设置')),
            ],
            options={
                'verbose_name': '系统设置',
                'verbose_name_plural': '系统设置',
            },
        ),
    ]