# Generated by Django 3.0.5 on 2020-04-15 06:13

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.contrib.taggit
import modelcluster.fields
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('wagtailimages', '0001_squashed_0021'),
        ('wagtailcore', '0045_assign_unlock_grouppagepermission'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('icon', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
            options={
                'verbose_name_plural': 'Категории (мепроприятия)',
            },
        ),
        migrations.CreateModel(
            name='EventIndex',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('calenadar_file', models.FileField(blank=True, null=True, upload_to='uploads/global_ics/')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='EventOrganizer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('email', models.EmailField(blank=True, max_length=40)),
                ('website', models.URLField(blank=True, help_text='Ссылка на сайт организатора')),
                ('phone', models.CharField(blank=True, max_length=19)),
                ('address', models.CharField(blank=True, max_length=50)),
                ('avatar', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
            options={
                'verbose_name_plural': 'Организаторы мероприятий',
            },
        ),
        migrations.CreateModel(
            name='EventPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('date', models.DateTimeField(verbose_name='Дата мероприятия')),
                ('dateend', models.DateTimeField(blank=True, null=True, verbose_name='Конец мероприятия')),
                ('cost', models.PositiveIntegerField(blank=True, help_text='Если оставить поле пустым отобразится что мероприятие бесплатное', null=True)),
                ('duration', models.DurationField(blank=True, help_text='Если указана дата окончания мероприятия, это поле в приоритете. Формат ввода Дни Часы:Минуты:Секунды')),
                ('ics', models.FileField(blank=True, null=True, upload_to='uploads/')),
                ('intro', wagtail.core.fields.RichTextField()),
                ('body', wagtail.core.fields.StreamField([('emphasize', wagtail.core.blocks.CharBlock(icon='title', label='Выделить текст', template='blocks/event_emphasize_block.html')), ('paragraph', wagtail.core.blocks.RichTextBlock(icon='pilcrow', label='Текст', template='blocks/event_paragraph_block.html')), ('image', wagtail.images.blocks.ImageChooserBlock(icon='image', label='Картинка справа', template='blocks/image_right_block.html')), ('html', wagtail.core.blocks.RawHTMLBlock(icon='code', label='Чистый HTML')), ('list', wagtail.core.blocks.ListBlock(wagtail.core.blocks.CharBlock(icon='list-ul', label='Пункт списка', template='blocks/list_block.html'))), ('blockquote', wagtail.core.blocks.StructBlock([('quote', wagtail.core.blocks.BlockQuoteBlock(label='Цитата')), ('author', wagtail.core.blocks.CharBlock(label='Автор'))], icon='openquote', template='blocks/quote_block.html'))])),
                ('max_visitors', models.PositiveIntegerField(blank=True)),
                ('location', models.CharField(blank=True, max_length=250)),
                ('timepad', models.URLField(blank=True, help_text='URL на мероприятие в Timepad')),
                ('views', models.IntegerField(default=0)),
                ('categories', modelcluster.fields.ParentalManyToManyField(blank=True, to='event.EventCategory')),
                ('main_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('organizer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='event.EventOrganizer')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='EventPageTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_object', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='tagged_items', to='event.EventPage')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_eventpagetag_items', to='taggit.Tag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EventPageRelatedLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('event_page', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='wagtailcore.Page')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_links', to='event.EventPage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='eventpage',
            name='tags',
            field=modelcluster.contrib.taggit.ClusterTaggableManager(blank=True, help_text='A comma-separated list of tags.', through='event.EventPageTag', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
