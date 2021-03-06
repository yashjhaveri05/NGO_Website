# Generated by Django 3.1.1 on 2020-09-22 06:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_redeem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image1', models.ImageField(default='default.png', upload_to='images/')),
                ('image2', models.ImageField(default='default.png', upload_to='images/')),
                ('image3', models.ImageField(default='default.png', upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('details', models.TextField()),
                ('awards', models.TextField(blank=True)),
                ('funds_used', models.FloatField()),
                ('event', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.event')),
                ('images', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.images')),
            ],
        ),
    ]
