# Generated by Django 3.2 on 2021-04-30 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0003_auto_20210428_1549'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluno',
            name='foto',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
