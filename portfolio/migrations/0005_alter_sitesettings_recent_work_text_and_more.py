# Generated by Django 5.1.4 on 2024-12-20 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_sitesettings_recent_work_text_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitesettings',
            name='recent_work_text',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='sitesettings',
            name='say_hi_text',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]
