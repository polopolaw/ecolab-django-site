# Generated by Django 3.0.5 on 2020-04-17 17:07

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0045_assign_unlock_grouppagepermission'),
        ('gallery', '0002_auto_20200417_1707'),
    ]

    operations = [
        migrations.AddField(
            model_name='galleryindex',
            name='collection',
            field=models.ForeignKey(help_text='Показывать изображения в галерее из этой коллекции.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.Collection', verbose_name='Collection'),
        ),
        migrations.AddField(
            model_name='galleryindex',
            name='images_per_page',
            field=models.IntegerField(default=8, help_text='Как много картинок отображать на странице.', verbose_name='Картинок на страницу'),
        ),
        migrations.AddField(
            model_name='galleryindex',
            name='intro_text',
            field=wagtail.core.fields.RichTextField(blank=True, help_text='Необязательное введение после заголовка.', verbose_name='Вводный текст'),
        ),
    ]
