# Generated by Django 4.2 on 2023-04-17 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scores', '0002_remove_match_pool_remove_pool_teams_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pool',
            name='name',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
    ]