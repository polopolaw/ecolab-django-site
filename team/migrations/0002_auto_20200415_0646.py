# Generated by Django 3.0.5 on 2020-04-15 06:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
        ('blog', '0001_initial'),
        ('wagtailforms', '0004_add_verbose_name_plural'),
        ('wagtailredirects', '0006_redirect_increase_max_length'),
        ('site_settings', '0001_initial'),
        ('wagtailcore', '0045_assign_unlock_grouppagepermission'),
        ('wagtailmenus', '0023_remove_use_specific'),
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teammember',
            name='role',
        ),
        migrations.DeleteModel(
            name='TeamIndex',
        ),
        migrations.DeleteModel(
            name='TeamMember',
        ),
        migrations.DeleteModel(
            name='TeamMemberRole',
        ),
    ]
