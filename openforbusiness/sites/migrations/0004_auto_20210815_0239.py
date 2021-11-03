# Generated by Django 3.2.4 on 2021-08-15 02:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0003_auto_20210815_0235'),
    ]

    operations = [
        migrations.RenameField(
            model_name='businessicon',
            old_name='business_clasification',
            new_name='business',
        ),
        migrations.AlterField(
            model_name='business',
            name='icon',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='icons', to='sites.businessicon'),
        ),
    ]