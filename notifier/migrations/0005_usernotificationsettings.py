# Generated by Django 4.0.2 on 2022-02-15 03:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0031_alter_employee_user_alter_employer_user'),
        ('notifier', '0004_hotemployeralert'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserNotificationSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.BooleanField(default=True)),
                ('login', models.BooleanField(default=True)),
                ('update', models.BooleanField(default=True)),
                ('newsletter', models.BooleanField(default=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_notification_settings', to='api.user')),
            ],
        ),
    ]