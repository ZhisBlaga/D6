# Generated by Django 3.0.7 on 2020-08-27 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='img',
            field=models.ImageField(blank=True, upload_to='book_img/%Y/%m/%d'),
        ),
    ]