# Generated by Django 4.0.7 on 2022-12-11 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0010_article_picture'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='profile',
            new_name='username',
        ),
        migrations.AlterField(
            model_name='article',
            name='picture',
            field=models.ImageField(upload_to='pictures'),
        ),
    ]