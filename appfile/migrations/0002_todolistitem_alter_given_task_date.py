# Generated by Django 4.0.2 on 2022-02-21 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appfile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TodoListItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tsk', models.TextField()),
                ('content', models.TextField(blank=True)),
            ],
        ),
        migrations.AlterField(
            model_name='given_task',
            name='date',
            field=models.DateField(),
        ),
    ]
