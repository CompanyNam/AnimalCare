# Generated by Django 2.1.2 on 2019-03-28 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_remove_menu_home'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='home',
            field=models.CharField(default=1, max_length=122),
            preserve_default=False,
        ),
    ]