# Generated by Django 5.1.4 on 2025-01-28 00:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_alter_image_image'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Image',
            new_name='Image_user',
        ),
        migrations.AlterModelOptions(
            name='image_user',
            options={'verbose_name': 'Image', 'verbose_name_plural': 'Images'},
        ),
    ]