# Generated by Django 2.1.2 on 2019-03-08 15:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('home', models.CharField(max_length=122)),
                ('gallery', models.CharField(max_length=122)),
                ('about', models.CharField(max_length=122)),
                ('events', models.CharField(max_length=122)),
                ('pages', models.CharField(max_length=122)),
                ('blog', models.CharField(max_length=122)),
                ('contact', models.CharField(max_length=122)),
            ],
        ),
        migrations.CreateModel(
            name='MenuLanguages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Menu')),
            ],
        ),
    ]