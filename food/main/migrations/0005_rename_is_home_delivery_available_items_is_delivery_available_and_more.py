# Generated by Django 4.2.7 on 2023-11-24 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_items_img_items_is_home_delivery_available'),
    ]

    operations = [
        migrations.RenameField(
            model_name='items',
            old_name='is_home_delivery_available',
            new_name='is_delivery_available',
        ),
        migrations.RemoveField(
            model_name='items',
            name='id',
        ),
        migrations.AlterField(
            model_name='items',
            name='name',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
