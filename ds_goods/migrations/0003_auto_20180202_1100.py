# Generated by Django 2.0.1 on 2018-02-02 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ds_goods', '0002_auto_20180202_0906'),
    ]

    operations = [
        migrations.AddField(
            model_name='typeinfo',
            name='pid',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='goodinfo',
            name='gtype',
            field=models.ForeignKey(on_delete=None, to='ds_goods.TypeInfo'),
        ),
    ]
