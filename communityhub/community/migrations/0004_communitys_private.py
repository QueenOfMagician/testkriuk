# Generated by Django 4.1.7 on 2023-08-22 11:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("community", "0003_remove_members_member_members_member"),
    ]

    operations = [
        migrations.AddField(
            model_name="communitys",
            name="private",
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]