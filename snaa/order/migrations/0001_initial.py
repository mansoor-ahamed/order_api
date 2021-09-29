# Generated by Django 3.2.4 on 2021-09-25 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=250)),
                ('price', models.CharField(max_length=50)),
                ('stock', models.CharField(max_length=50)),
                ('is_active', models.BooleanField(blank=True, default=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('specification', models.CharField(max_length=250)),
                ('order_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
