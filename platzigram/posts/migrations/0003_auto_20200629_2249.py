# Generated by Django 3.0.7 on 2020-06-29 22:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_user_is_admin'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='uodated',
            new_name='updated',
        ),
    ]