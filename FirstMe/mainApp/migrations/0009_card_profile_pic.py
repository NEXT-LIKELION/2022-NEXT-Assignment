# Generated by Django 4.0.4 on 2022-05-26 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0008_alter_friendlists_friends_alter_groups_members'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='profile_pic',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
