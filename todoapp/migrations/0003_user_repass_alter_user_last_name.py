# Generated by Django 4.0.5 on 2022-06-10 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0002_alter_user_last_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='repass',
            field=models.TextField(max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='last name'),
        ),
    ]
