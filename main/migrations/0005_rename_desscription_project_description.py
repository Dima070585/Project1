# Generated by Django 3.2.5 on 2021-07-19 16:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_post_prise'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='desscription',
            new_name='description',
        ),
    ]
