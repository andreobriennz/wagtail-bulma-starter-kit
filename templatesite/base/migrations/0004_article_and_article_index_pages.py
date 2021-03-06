# Generated by Django 3.2.9 on 2022-04-30 11:09

import base.blocks
from django.db import migrations, models
import django.db.models.deletion
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0066_collection_management_permissions'),
        ('base', '0003_homepage_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='standardpage',
            name='banner_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='base.customimage'),
        ),
        migrations.AddField(
            model_name='standardpage',
            name='content',
            field=wagtail.fields.StreamField([('text', wagtail.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'bold', 'ol', 'ul', 'link', 'document-link', 'br'], template='blocks/richtext_block.html')), ('image_block', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True))])), ('video_block', wagtail.blocks.StructBlock([('url', wagtail.blocks.CharBlock(required=True))])), ('card_list_block', wagtail.blocks.StructBlock([('items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('text', wagtail.blocks.CharBlock(required=False))])))])), ('accordion_block', wagtail.blocks.StructBlock([('items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(required=True)), ('content', wagtail.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'bold', 'ol', 'ul', 'link', 'document-link', 'br'], template='blocks/richtext_block.html'))])))])), ('horizontal_rule', base.blocks.HorizontalRuleBlock())], blank=True, verbose_name='Main Content'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='content',
            field=wagtail.fields.StreamField([('text', wagtail.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'bold', 'ol', 'ul', 'link', 'document-link', 'br'], template='blocks/richtext_block.html')), ('image_block', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True))])), ('video_block', wagtail.blocks.StructBlock([('url', wagtail.blocks.CharBlock(required=True))])), ('card_list_block', wagtail.blocks.StructBlock([('items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('text', wagtail.blocks.CharBlock(required=False))])))])), ('accordion_block', wagtail.blocks.StructBlock([('items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(required=True)), ('content', wagtail.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'bold', 'ol', 'ul', 'link', 'document-link', 'br'], template='blocks/richtext_block.html'))])))])), ('horizontal_rule', base.blocks.HorizontalRuleBlock())], blank=True, verbose_name='Main Content'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='subtitle',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='standardpage',
            name='subtitle',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.CreateModel(
            name='ArticlePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('subtitle', models.CharField(blank=True, max_length=255, null=True)),
                ('content', wagtail.fields.StreamField([('text', wagtail.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'bold', 'ol', 'ul', 'link', 'document-link', 'br'], template='blocks/richtext_block.html')), ('image_block', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True))])), ('video_block', wagtail.blocks.StructBlock([('url', wagtail.blocks.CharBlock(required=True))])), ('card_list_block', wagtail.blocks.StructBlock([('items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('text', wagtail.blocks.CharBlock(required=False))])))])), ('accordion_block', wagtail.blocks.StructBlock([('items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(required=True)), ('content', wagtail.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'bold', 'ol', 'ul', 'link', 'document-link', 'br'], template='blocks/richtext_block.html'))])))])), ('horizontal_rule', base.blocks.HorizontalRuleBlock())], blank=True, verbose_name='Main Content')),
                ('banner_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='base.customimage')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='ArticleIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('subtitle', models.CharField(blank=True, max_length=255, null=True)),
                ('banner_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='base.customimage')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
