# Generated by Django 4.0.6 on 2022-08-09 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_product_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sname', models.CharField(max_length=50)),
            ],
        ),
    ]