# Generated by Django 4.2.11 on 2024-06-18 07:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('edited', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('DRA', 'Draft'), ('PUB', 'Published'), ('DEL', 'Deleted')], default='DRA', max_length=3)),
                ('slug', models.SlugField(max_length=250, unique=True)),
                ('surname', models.CharField(max_length=250)),
                ('name', models.CharField(blank=True, max_length=250)),
                ('born', models.DateField(blank=True, null=True)),
                ('died', models.DateField(blank=True, null=True)),
                ('occupation', models.CharField(blank=True, max_length=250)),
                ('citizenship', models.CharField(blank=True, max_length=250)),
                ('biography', models.TextField(blank=True)),
                ('image', models.ImageField(default='placeholder.jpg', upload_to='authors')),
                ('creator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('editor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['surname'],
            },
        ),
    ]
