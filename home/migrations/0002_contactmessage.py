# Generated by Django 3.2.2 on 2021-05-20 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('message', models.CharField(blank=True, max_length=300, null=True)),
                ('notes', models.CharField(blank=True, max_length=100)),
                ('status', models.CharField(choices=[('New', 'New'), ('Read', 'Read'), ('pending', 'pending'), ('Closed', 'Closed')], default='New', max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]