# Generated by Django 5.0.7 on 2024-09-29 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topic', '0008_glossary'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=120, verbose_name='Email')),
                ('message', models.TextField()),
            ],
            options={
                'verbose_name': 'Contact Us',
                'verbose_name_plural': 'Contact Us',
            },
        ),
    ]
