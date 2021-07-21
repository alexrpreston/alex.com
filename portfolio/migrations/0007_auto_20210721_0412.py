# Generated by Django 3.1.1 on 2021-07-21 04:12

from django.db import migrations, models
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_book_year'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='year',
        ),
        migrations.AddField(
            model_name='book',
            name='notes',
            field=markdownx.models.MarkdownxField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='slug',
            field=models.SlugField(default=0, max_length=200, unique=True),
            preserve_default=False,
        ),
    ]
