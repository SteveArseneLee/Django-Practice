# Generated by Django 3.2.6 on 2021-08-26 09:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='board',
            options={'verbose_name': '게시글', 'verbose_name_plural': '게시글들'},
        ),
        migrations.RenameField(
            model_name='board',
            old_name='register_dttm',
            new_name='registered_dttm',
        ),
    ]
