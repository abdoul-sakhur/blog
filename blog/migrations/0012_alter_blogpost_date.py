# Generated by Django 5.0.6 on 2024-06-17 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_remove_blogpost_category_blogpost_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='date',
            field=models.DateField(auto_created=True, blank=True, null=True),
        ),
    ]
