# Generated by Django 4.2.6 on 2023-12-14 09:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0006_form_link_formdata'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='form',
            name='link',
        ),
        migrations.DeleteModel(
            name='FormData',
        ),
    ]
