# Generated by Django 3.0.5 on 2020-04-15 06:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0045_assign_unlock_grouppagepermission'),
        ('team', '0002_auto_20200415_0646'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamIndex',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='TeamMemberRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, null=True)),
                ('plural', models.CharField(help_text='Название во множественном числе', max_length=40, null=True)),
            ],
            options={
                'verbose_name_plural': 'Роль в команде проекта',
            },
        ),
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info', models.CharField(blank=True, max_length=100)),
                ('specificrole', models.CharField(blank=True, max_length=100)),
                ('facebook', models.URLField(blank=True, help_text='Your Facebook page URL')),
                ('instagram', models.CharField(blank=True, help_text='Your Instagram username, without the @', max_length=255)),
                ('twitter', models.URLField(blank=True, help_text='URL на аккаунт в Twitter')),
                ('vk', models.URLField(blank=True, help_text='URL vk.com')),
                ('role', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='team.TeamMemberRole')),
            ],
            options={
                'verbose_name_plural': 'Команда проекта',
            },
        ),
    ]
