# Generated by Django 4.2.7 on 2023-11-27 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0005_alter_note_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='file',
            field=models.FileField(upload_to='item_images'),
        ),
    ]
