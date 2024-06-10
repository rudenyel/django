# Generated by Django 4.2.11 on 2024-06-09 19:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('authors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('edited', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('DRA', 'Draft'), ('PUB', 'Published'), ('DEL', 'Deleted')], default='DRA', max_length=3)),
                ('slug', models.SlugField(max_length=250, unique=True)),
                ('title', models.CharField(max_length=250)),
                ('finished', models.DateField(blank=True, null=True)),
                ('authors', models.ManyToManyField(blank=True, related_name='books', related_query_name='book', to='authors.author')),
                ('creator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('editor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['title'],
                'indexes': [models.Index(fields=['title'], name='books_book_title_d3218d_idx')],
            },
        ),
    ]
