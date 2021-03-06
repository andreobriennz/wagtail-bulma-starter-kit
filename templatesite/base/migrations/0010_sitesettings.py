# Generated by Django 3.2.9 on 2022-05-09 01:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0066_collection_management_permissions'),
        ('base', '0009_remove_display_breadcrumbs'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seo_site_description', models.CharField(help_text='Used by search engines when there is not a specific description for the page. Should be between 50 and 160 characters (any longer and the text may be truncated by many search engines.', max_length=160, null=True)),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.site')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
