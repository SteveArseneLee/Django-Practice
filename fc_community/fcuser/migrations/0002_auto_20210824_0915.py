# Generated by Django 3.2.6 on 2021-08-24 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fcuser', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fcuser',
            options={'verbose_name': '사용자', 'verbose_name_plural': '사용자 목록'},
        ),
        migrations.AddField(
            model_name='fcuser',
            name='useremail',
            field=models.EmailField(default='test@gmail.com', max_length=128, verbose_name='사용자이메일'),
            preserve_default=False,
        ),
    ]