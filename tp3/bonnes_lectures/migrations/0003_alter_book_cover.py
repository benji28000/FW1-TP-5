# Generated by Django 4.2.16 on 2024-10-23 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bonnes_lectures', '0002_alter_book_cover_alter_book_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover',
            field=models.FileField(null=True, upload_to='images/'),
        ),
    ]