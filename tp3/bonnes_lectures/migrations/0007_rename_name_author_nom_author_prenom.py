# Generated by Django 4.2.16 on 2024-11-12 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bonnes_lectures', '0006_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='name',
            new_name='nom',
        ),
        migrations.AddField(
            model_name='author',
            name='prenom',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
