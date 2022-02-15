# Generated by Django 3.2.8 on 2021-12-23 18:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0019_auto_20211223_1838'),
        ('notifier', '0002_auto_20211211_1941'),
    ]

    operations = [
        migrations.CreateModel(
            name='HotEmployeeAlert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=200)),
                ('link', models.CharField(choices=[['profile', 'profile'], ['interview', 'interview'], ['inbox', 'inbox']], max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('employee', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.employee')),
            ],
        ),
    ]