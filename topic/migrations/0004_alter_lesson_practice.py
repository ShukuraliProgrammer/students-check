# Generated by Django 4.0.5 on 2022-07-03 06:13

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('topic', '0003_alter_lesson_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='practice',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]