# Generated by Django 5.1.4 on 2024-12-29 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_rename_img_maininformations_img_back_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='maininformations',
            name='current_work',
            field=models.CharField(max_length=255, null=True, verbose_name='Current workplace'),
        ),
    ]