# Generated by Django 4.0.2 on 2022-02-21 19:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appfile', '0002_todolistitem_alter_given_task_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todolistitem',
            name='content',
        ),
    ]
