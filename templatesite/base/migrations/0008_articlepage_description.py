# Generated by Django 3.2.9 on 2022-05-04 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_contactsettings_imagesettings'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlepage',
            name='description',
            field=models.CharField(blank=True, help_text='Used in cards which link to the article (not the article itself)', max_length=255, null=True),
        ),
    ]
