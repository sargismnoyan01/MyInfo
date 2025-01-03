# Generated by Django 5.1.4 on 2024-12-30 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_abouttxt'),
    ]

    operations = [
        migrations.CreateModel(
            name='StaffStory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.ImageField(upload_to='icon', verbose_name='Icone')),
                ('position', models.CharField(max_length=255, verbose_name='Position')),
                ('info', models.TextField(verbose_name='Information')),
            ],
            options={
                'verbose_name': 'Staff story',
                'verbose_name_plural': 'Staff story',
            },
        ),
    ]
