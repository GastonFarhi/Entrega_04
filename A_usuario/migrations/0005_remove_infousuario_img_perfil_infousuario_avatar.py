# Generated by Django 5.2 on 2025-04-28 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('A_usuario', '0004_alter_infousuario_img_perfil'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='infousuario',
            name='img_perfil',
        ),
        migrations.AddField(
            model_name='infousuario',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatars'),
        ),
    ]
