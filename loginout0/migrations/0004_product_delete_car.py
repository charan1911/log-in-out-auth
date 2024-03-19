# Generated by Django 4.1.13 on 2024-03-19 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginout0', '0003_car_delete_userr'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('picture', models.ImageField(upload_to='product_pictures/')),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.DeleteModel(
            name='car',
        ),
    ]
