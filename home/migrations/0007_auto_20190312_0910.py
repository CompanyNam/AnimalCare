# Generated by Django 2.1.2 on 2019-03-12 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_animal_need_help'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='image',
        ),
        migrations.AddField(
            model_name='event',
            name='animal_image1',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='event',
            name='animal_image10',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='event',
            name='animal_image11',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='event',
            name='animal_image12',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='event',
            name='animal_image13',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='event',
            name='animal_image2',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='event',
            name='animal_image3',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='event',
            name='animal_image4',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='event',
            name='animal_image5',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='event',
            name='animal_image6',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='event',
            name='animal_image7',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='event',
            name='animal_image8',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='event',
            name='animal_image9',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='event',
            name='image_main',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]