# Generated by Django 4.0.5 on 2022-07-30 18:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0005_album'),
    ]

    operations = [
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('image', models.ImageField(upload_to='picture/%Y/%m/%d/')),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gallery.album')),
            ],
        ),
    ]
