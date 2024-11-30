# Generated by Django 5.1.3 on 2024-11-30 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_remove_user_fullname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chat',
            name='admins',
        ),
        migrations.AddField(
            model_name='userschats',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
    ]