# Generated by Django 2.2.5 on 2020-05-31 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comic', '0003_remove_chapter_pages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapter',
            name='chapter_pages',
            field=models.IntegerField(default=14),
        ),
    ]