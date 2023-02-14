# Generated by Django 4.0.4 on 2023-02-13 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_remove_order_cost_remove_order_total_items'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='desc',
        ),
        migrations.AddField(
            model_name='product',
            name='is_special',
            field=models.BooleanField(default=False, null=True),
        ),
    ]