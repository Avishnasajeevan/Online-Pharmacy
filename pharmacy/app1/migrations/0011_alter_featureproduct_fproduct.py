# Generated by Django 4.0.6 on 2022-08-10 04:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0010_featureproduct'),
    ]

    operations = [
        migrations.AlterField(
            model_name='featureproduct',
            name='fproduct',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app1.product'),
        ),
    ]
