# Generated by Django 2.0.2 on 2018-03-02 07:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=300)),
                ('body', models.CharField(max_length=1000)),
                ('sender_deleted', models.BooleanField(default=False)),
                ('target_deleted', models.BooleanField(default=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='message_sender', to='server.Account')),
                ('target', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='message_target', to='server.Account')),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=200)),
                ('read', models.BooleanField(default=False)),
                ('sent_timestamp', models.DateTimeField(auto_now_add=True)),
                ('read_timestamp', models.DateTimeField(blank=True, null=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notifications_account', to='server.Account')),
            ],
        ),
    ]
