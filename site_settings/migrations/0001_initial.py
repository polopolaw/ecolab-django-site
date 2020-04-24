# Generated by Django 3.0.5 on 2020-04-15 06:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0045_assign_unlock_grouppagepermission'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubscribeFormSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.Site')),
                ('subscribe_form_page', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='wagtailcore.Page')),
            ],
            options={
                'verbose_name': 'Форма подписки email',
            },
        ),
        migrations.CreateModel(
            name='SocialMediaSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook', models.URLField(blank=True, help_text='Your Facebook page URL')),
                ('instagram', models.CharField(blank=True, help_text='Your Instagram username, without the @', max_length=255)),
                ('youtube', models.URLField(blank=True, help_text='Your YouTube channel or user account URL')),
                ('twitter', models.URLField(blank=True, help_text='URL на аккаунт в Twitter')),
                ('vk', models.URLField(blank=True, help_text='URL vk.com')),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.Site')),
            ],
            options={
                'verbose_name': 'Аккаунты в социальных сетях',
            },
        ),
    ]