# Generated by Django 3.0 on 2021-01-24 22:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tales', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['name']},
        ),
        migrations.RenameField(
            model_name='image',
            old_name='image_category',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='image',
            old_name='image_description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='image',
            old_name='image_location',
            new_name='location',
        ),
        migrations.RenameField(
            model_name='image',
            old_name='image_name',
            new_name='name',
        ),
    ]
