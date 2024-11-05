# Generated by Django 4.2.16 on 2024-10-23 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bonnes_lectures', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover',
            field=models.FileField(null=True, upload_to='images/', verbose_name='Title image'),
        ),
        migrations.AlterField(
            model_name='book',
            name='year',
            field=models.DateField(),
        ),
    ]