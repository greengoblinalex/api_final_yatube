# Generated by Django 3.2.16 on 2023-04-10 16:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_follow_unique_user_following'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='follow',
            name='unique_user_following',
        ),
    ]
