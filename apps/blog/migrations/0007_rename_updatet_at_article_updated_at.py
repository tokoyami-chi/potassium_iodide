# Generated by Django 4.1.3 on 2022-11-25 16:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_article_tag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='updated_at',
            new_name='updated_at',
        ),
    ]
