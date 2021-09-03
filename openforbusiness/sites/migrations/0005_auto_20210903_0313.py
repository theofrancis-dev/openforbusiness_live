# Generated by Django 3.2.4 on 2021-09-03 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0004_auto_20210815_0239'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='card_image',
            field=models.ImageField(blank=True, null=True, upload_to='business_images/'),
        ),
        migrations.AddField(
            model_name='business',
            name='description_line_1',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='business',
            name='description_line_2',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='business',
            name='facebook',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='business',
            name='instagram',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='business',
            name='tweeter',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='business',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='business',
            name='image1',
            field=models.ImageField(blank=True, null=True, upload_to='business_images/'),
        ),
        migrations.AlterField(
            model_name='business',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='business_images/'),
        ),
        migrations.AlterField(
            model_name='business',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to='business_images/'),
        ),
    ]
