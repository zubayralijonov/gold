# Generated by Django 4.2.7 on 2024-02-12 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.TextField(max_length=60)),
                ('first_name', models.TextField(max_length=60)),
                ('age', models.TextField()),
            ],
        ),
    ]
