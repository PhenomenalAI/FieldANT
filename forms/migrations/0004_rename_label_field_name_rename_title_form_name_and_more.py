# Generated by Django 4.2.6 on 2023-12-12 11:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0003_field_submission_remove_form_unique_url_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='field',
            old_name='label',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='form',
            old_name='title',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='field',
            name='form',
        ),
        migrations.RemoveField(
            model_name='field',
            name='options',
        ),
        migrations.RemoveField(
            model_name='field',
            name='order',
        ),
        migrations.RemoveField(
            model_name='field',
            name='type',
        ),
        migrations.RemoveField(
            model_name='form',
            name='link',
        ),
        migrations.AddField(
            model_name='field',
            name='data_type',
            field=models.CharField(choices=[('CHAR', 'Char'), ('INTEGER', 'Integer'), ('FLOAT', 'Float'), ('BOOLEAN', 'Boolean')], default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='form',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='form',
            name='fields',
            field=models.ManyToManyField(related_name='forms', to='forms.field'),
        ),
        migrations.AlterField(
            model_name='field',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='form',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.DeleteModel(
            name='Submission',
        ),
    ]