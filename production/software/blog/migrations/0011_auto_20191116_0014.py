# Generated by Django 2.2.6 on 2019-11-15 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20191115_2359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='image',
            field=models.ImageField(blank=True, upload_to='shop/images'),
        ),
    ]
