# Generated by Django 4.1.3 on 2022-11-20 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogCategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Назва категорії')),
            ],
            options={
                'verbose_name': 'Категорія блогу',
                'verbose_name_plural': 'Категорії блогу',
            },
        ),
    ]
