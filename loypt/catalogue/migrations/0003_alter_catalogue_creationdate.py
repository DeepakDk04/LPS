# Generated by Django 5.1.3 on 2024-11-15 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0002_alter_catalogue_vendor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalogue',
            name='creationDate',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]