# Generated by Django 5.1.3 on 2024-11-29 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_phone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chat',
            old_name='name',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='user',
            name='tg_id',
        ),
        migrations.AddField(
            model_name='chat',
            name='admins',
            field=models.JSONField(null=True),
        ),
        migrations.AddField(
            model_name='chat',
            name='avatar_url',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='chat',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='chat',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='chat',
            name='url',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
