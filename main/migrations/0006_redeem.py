# Generated by Django 3.1.1 on 2020-09-21 17:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20200921_2210'),
    ]

    operations = [
        migrations.CreateModel(
            name='Redeem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('brand', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('price', models.IntegerField(default=0)),
                ('image', models.ImageField(default='default1.png', upload_to='images/')),
                ('created', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
