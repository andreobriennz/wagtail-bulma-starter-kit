# Generated by Django 4.0.4 on 2022-05-20 01:44

import base.blocks
from django.db import migrations
import wagtail.admin.forms.choosers
import wagtail.blocks
import wagtail.fields
import wagtail.documents.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_delete_styleguidepage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlepage',
            name='content',
            field=wagtail.fields.StreamField([('text', wagtail.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'bold', 'ol', 'ul', 'link', 'document-link', 'br'], template='blocks/richtext_block.html')), ('buttons_block', wagtail.blocks.StructBlock([('items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('text', wagtail.blocks.CharBlock(required=True)), ('style', wagtail.blocks.ChoiceBlock(blank=True, choices=[('primary', 'Primary'), ('secondary', 'Secondary')])), ('link', wagtail.blocks.StructBlock([('link_to', wagtail.blocks.ChoiceBlock(choices=[('page', 'Page'), ('file', 'File'), ('custom_url', 'Custom URL')], classname='link_choice_type_selector', label='Link to', required=False)), ('page', wagtail.blocks.PageChooserBlock(form_classname='page_link', label='Page', required=False)), ('file', wagtail.documents.blocks.DocumentChooserBlock(form_classname='file_link', label='File', required=False)), ('custom_url', wagtail.blocks.CharBlock(form_classname='custom_url_link url_field', label='Custom URL', max_length=300, required=False, validators=[wagtail.admin.forms.choosers.URLOrAbsolutePathValidator()])), ('new_window', wagtail.blocks.BooleanBlock(form_classname='new_window_toggle', label='Open in new window', required=False))]))], blank=True, required=False), blank=True))])), ('image_block', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True))])), ('cta_banner_block', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='A banner which is 50% width on desktop (use photos which are at least 960x600px).', required=True)), ('image_side', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('right', 'Right')])), ('title', wagtail.blocks.CharBlock(required=False)), ('text', wagtail.blocks.RichTextBlock(features=['bold', 'br'], required=False, template='blocks/richtext_block.html')), ('buttons', wagtail.blocks.StructBlock([('items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('text', wagtail.blocks.CharBlock(required=True)), ('style', wagtail.blocks.ChoiceBlock(blank=True, choices=[('primary', 'Primary'), ('secondary', 'Secondary')])), ('link', wagtail.blocks.StructBlock([('link_to', wagtail.blocks.ChoiceBlock(choices=[('page', 'Page'), ('file', 'File'), ('custom_url', 'Custom URL')], classname='link_choice_type_selector', label='Link to', required=False)), ('page', wagtail.blocks.PageChooserBlock(form_classname='page_link', label='Page', required=False)), ('file', wagtail.documents.blocks.DocumentChooserBlock(form_classname='file_link', label='File', required=False)), ('custom_url', wagtail.blocks.CharBlock(form_classname='custom_url_link url_field', label='Custom URL', max_length=300, required=False, validators=[wagtail.admin.forms.choosers.URLOrAbsolutePathValidator()])), ('new_window', wagtail.blocks.BooleanBlock(form_classname='new_window_toggle', label='Open in new window', required=False))]))], blank=True, required=False), blank=True))], blank=True, required=False))])), ('video_block', wagtail.blocks.StructBlock([('url', wagtail.blocks.CharBlock(help_text='A link to a video on YouTube or Vimeo (eg https://www.youtube.com/embed/YE7VzlLtp-4).', required=True))])), ('card_list_block', wagtail.blocks.StructBlock([('items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('text', wagtail.blocks.CharBlock(required=False))])))])), ('accordion_block', wagtail.blocks.StructBlock([('items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(required=True)), ('content', wagtail.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'bold', 'ol', 'ul', 'link', 'document-link', 'br'], template='blocks/richtext_block.html'))])))])), ('horizontal_rule', base.blocks.HorizontalRuleBlock())], blank=True, verbose_name='Main Content'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='content',
            field=wagtail.fields.StreamField([('text', wagtail.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'bold', 'ol', 'ul', 'link', 'document-link', 'br'], template='blocks/richtext_block.html')), ('buttons_block', wagtail.blocks.StructBlock([('items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('text', wagtail.blocks.CharBlock(required=True)), ('style', wagtail.blocks.ChoiceBlock(blank=True, choices=[('primary', 'Primary'), ('secondary', 'Secondary')])), ('link', wagtail.blocks.StructBlock([('link_to', wagtail.blocks.ChoiceBlock(choices=[('page', 'Page'), ('file', 'File'), ('custom_url', 'Custom URL')], classname='link_choice_type_selector', label='Link to', required=False)), ('page', wagtail.blocks.PageChooserBlock(form_classname='page_link', label='Page', required=False)), ('file', wagtail.documents.blocks.DocumentChooserBlock(form_classname='file_link', label='File', required=False)), ('custom_url', wagtail.blocks.CharBlock(form_classname='custom_url_link url_field', label='Custom URL', max_length=300, required=False, validators=[wagtail.admin.forms.choosers.URLOrAbsolutePathValidator()])), ('new_window', wagtail.blocks.BooleanBlock(form_classname='new_window_toggle', label='Open in new window', required=False))]))], blank=True, required=False), blank=True))])), ('image_block', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True))])), ('cta_banner_block', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='A banner which is 50% width on desktop (use photos which are at least 960x600px).', required=True)), ('image_side', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('right', 'Right')])), ('title', wagtail.blocks.CharBlock(required=False)), ('text', wagtail.blocks.RichTextBlock(features=['bold', 'br'], required=False, template='blocks/richtext_block.html')), ('buttons', wagtail.blocks.StructBlock([('items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('text', wagtail.blocks.CharBlock(required=True)), ('style', wagtail.blocks.ChoiceBlock(blank=True, choices=[('primary', 'Primary'), ('secondary', 'Secondary')])), ('link', wagtail.blocks.StructBlock([('link_to', wagtail.blocks.ChoiceBlock(choices=[('page', 'Page'), ('file', 'File'), ('custom_url', 'Custom URL')], classname='link_choice_type_selector', label='Link to', required=False)), ('page', wagtail.blocks.PageChooserBlock(form_classname='page_link', label='Page', required=False)), ('file', wagtail.documents.blocks.DocumentChooserBlock(form_classname='file_link', label='File', required=False)), ('custom_url', wagtail.blocks.CharBlock(form_classname='custom_url_link url_field', label='Custom URL', max_length=300, required=False, validators=[wagtail.admin.forms.choosers.URLOrAbsolutePathValidator()])), ('new_window', wagtail.blocks.BooleanBlock(form_classname='new_window_toggle', label='Open in new window', required=False))]))], blank=True, required=False), blank=True))], blank=True, required=False))])), ('video_block', wagtail.blocks.StructBlock([('url', wagtail.blocks.CharBlock(help_text='A link to a video on YouTube or Vimeo (eg https://www.youtube.com/embed/YE7VzlLtp-4).', required=True))])), ('card_list_block', wagtail.blocks.StructBlock([('items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('text', wagtail.blocks.CharBlock(required=False))])))])), ('accordion_block', wagtail.blocks.StructBlock([('items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(required=True)), ('content', wagtail.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'bold', 'ol', 'ul', 'link', 'document-link', 'br'], template='blocks/richtext_block.html'))])))])), ('horizontal_rule', base.blocks.HorizontalRuleBlock())], blank=True, verbose_name='Main Content'),
        ),
        migrations.AlterField(
            model_name='standardpage',
            name='content',
            field=wagtail.fields.StreamField([('text', wagtail.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'bold', 'ol', 'ul', 'link', 'document-link', 'br'], template='blocks/richtext_block.html')), ('buttons_block', wagtail.blocks.StructBlock([('items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('text', wagtail.blocks.CharBlock(required=True)), ('style', wagtail.blocks.ChoiceBlock(blank=True, choices=[('primary', 'Primary'), ('secondary', 'Secondary')])), ('link', wagtail.blocks.StructBlock([('link_to', wagtail.blocks.ChoiceBlock(choices=[('page', 'Page'), ('file', 'File'), ('custom_url', 'Custom URL')], classname='link_choice_type_selector', label='Link to', required=False)), ('page', wagtail.blocks.PageChooserBlock(form_classname='page_link', label='Page', required=False)), ('file', wagtail.documents.blocks.DocumentChooserBlock(form_classname='file_link', label='File', required=False)), ('custom_url', wagtail.blocks.CharBlock(form_classname='custom_url_link url_field', label='Custom URL', max_length=300, required=False, validators=[wagtail.admin.forms.choosers.URLOrAbsolutePathValidator()])), ('new_window', wagtail.blocks.BooleanBlock(form_classname='new_window_toggle', label='Open in new window', required=False))]))], blank=True, required=False), blank=True))])), ('image_block', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True))])), ('cta_banner_block', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='A banner which is 50% width on desktop (use photos which are at least 960x600px).', required=True)), ('image_side', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('right', 'Right')])), ('title', wagtail.blocks.CharBlock(required=False)), ('text', wagtail.blocks.RichTextBlock(features=['bold', 'br'], required=False, template='blocks/richtext_block.html')), ('buttons', wagtail.blocks.StructBlock([('items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('text', wagtail.blocks.CharBlock(required=True)), ('style', wagtail.blocks.ChoiceBlock(blank=True, choices=[('primary', 'Primary'), ('secondary', 'Secondary')])), ('link', wagtail.blocks.StructBlock([('link_to', wagtail.blocks.ChoiceBlock(choices=[('page', 'Page'), ('file', 'File'), ('custom_url', 'Custom URL')], classname='link_choice_type_selector', label='Link to', required=False)), ('page', wagtail.blocks.PageChooserBlock(form_classname='page_link', label='Page', required=False)), ('file', wagtail.documents.blocks.DocumentChooserBlock(form_classname='file_link', label='File', required=False)), ('custom_url', wagtail.blocks.CharBlock(form_classname='custom_url_link url_field', label='Custom URL', max_length=300, required=False, validators=[wagtail.admin.forms.choosers.URLOrAbsolutePathValidator()])), ('new_window', wagtail.blocks.BooleanBlock(form_classname='new_window_toggle', label='Open in new window', required=False))]))], blank=True, required=False), blank=True))], blank=True, required=False))])), ('video_block', wagtail.blocks.StructBlock([('url', wagtail.blocks.CharBlock(help_text='A link to a video on YouTube or Vimeo (eg https://www.youtube.com/embed/YE7VzlLtp-4).', required=True))])), ('card_list_block', wagtail.blocks.StructBlock([('items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('text', wagtail.blocks.CharBlock(required=False))])))])), ('accordion_block', wagtail.blocks.StructBlock([('items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(required=True)), ('content', wagtail.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'bold', 'ol', 'ul', 'link', 'document-link', 'br'], template='blocks/richtext_block.html'))])))])), ('horizontal_rule', base.blocks.HorizontalRuleBlock())], blank=True, verbose_name='Main Content'),
        ),
    ]