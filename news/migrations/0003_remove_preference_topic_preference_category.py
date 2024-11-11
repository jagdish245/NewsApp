# Generated by Django 5.1.3 on 2024-11-08 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_user_groups_user_is_active_user_is_staff_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='preference',
            name='topic',
        ),
        migrations.AddField(
            model_name='preference',
            name='category',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]