# Generated by Django 2.2.6 on 2019-11-04 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('member_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('mobile_no', models.CharField(max_length=50)),
                ('description', models.CharField(default='', max_length=500)),
                ('meta_title', models.CharField(default='', max_length=70)),
                ('meta_desc', models.CharField(default='', max_length=500)),
                ('image', models.ImageField(default='', upload_to='shop/images')),
            ],
        ),
        migrations.CreateModel(
            name='NewsAndEvent',
            fields=[
                ('news_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(default='', max_length=500)),
                ('meta_title', models.CharField(default='', max_length=70)),
                ('meta_desc', models.CharField(default='', max_length=500)),
                ('image', models.ImageField(default='', upload_to='shop/images')),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('page_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(default='', max_length=500)),
                ('meta_title', models.CharField(default='', max_length=70)),
                ('meta_desc', models.CharField(default='', max_length=500)),
                ('image', models.ImageField(default='', upload_to='shop/images')),
            ],
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('testimonial_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(default='', max_length=500)),
                ('meta_title', models.CharField(default='', max_length=70)),
                ('meta_desc', models.CharField(default='', max_length=500)),
                ('image', models.ImageField(default='', upload_to='shop/images')),
            ],
        ),
        migrations.AddField(
            model_name='blogpost',
            name='thumbnail',
            field=models.ImageField(default='', upload_to='shop/images'),
        ),
    ]