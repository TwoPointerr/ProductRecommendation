# Generated by Django 3.2 on 2021-04-28 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210427_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='pincode',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='profiles/default.jpg', null=True, upload_to='profiles'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='mob_no',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
