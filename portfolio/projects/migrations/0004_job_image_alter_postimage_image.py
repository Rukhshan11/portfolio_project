# Generated by Django 4.1.5 on 2023-02-09 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_job_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='postimage',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
