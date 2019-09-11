# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-09-11 21:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import project.s3utils
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChatRoom',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, editable=False, max_length=1024, primary_key=True, serialize=False)),
                ('room', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Chat room',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, editable=False, max_length=1024, primary_key=True, serialize=False)),
                ('message', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.ChatRoom')),
            ],
            options={
                'verbose_name_plural': 'Chat Message',
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, editable=False, max_length=1024, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('message', models.TextField()),
                ('read', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='PostPhotos',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, editable=False, max_length=1024, primary_key=True, serialize=False)),
                ('image', models.FileField(storage=project.s3utils.PostPhotosStorage(), upload_to='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': '2.2. Post Photos',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, editable=False, max_length=1024, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('category', models.CharField(max_length=255)),
                ('condition', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.IntegerField(default=0)),
                ('negotiable', models.BooleanField(default=True)),
                ('city_town', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('sold', models.BooleanField(default=False)),
                ('premium', models.BooleanField(default=False)),
                ('posted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': '2.1. Posts',
                'ordering': ['-created_at', '-premium'],
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, editable=False, max_length=1024, primary_key=True, serialize=False)),
                ('review', models.TextField()),
                ('rating', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Account Reviews',
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, editable=False, max_length=1024, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': '1. Users',
            },
        ),
        migrations.CreateModel(
            name='UserAccount',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, editable=False, max_length=1024, primary_key=True, serialize=False)),
                ('image', models.FileField(blank=True, null=True, storage=project.s3utils.MediaStorage(), upload_to='')),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
                ('username', models.CharField(blank=True, max_length=255, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=255, null=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('password', models.CharField(blank=True, max_length=255, null=True)),
                ('token', models.CharField(default='', max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.User')),
            ],
            options={
                'verbose_name_plural': '1.2. User Account',
            },
        ),
        migrations.CreateModel(
            name='UserAccountFollowers',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, editable=False, max_length=1024, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follower', to='api.UserAccount')),
                ('following', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='following', to='api.UserAccount')),
            ],
            options={
                'verbose_name_plural': 'User Followers',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='UserSavedPosts',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, editable=False, max_length=1024, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.UserAccount')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Posts')),
            ],
            options={
                'verbose_name_plural': 'User Saved Posts',
                'ordering': ['-created_at'],
            },
        ),
        migrations.AddField(
            model_name='review',
            name='reviewee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviewee', to='api.UserAccount'),
        ),
        migrations.AddField(
            model_name='review',
            name='reviewer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviewer', to='api.UserAccount'),
        ),
        migrations.AddField(
            model_name='posts',
            name='account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.UserAccount'),
        ),
        migrations.AddField(
            model_name='postphotos',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Posts'),
        ),
        migrations.AddField(
            model_name='notification',
            name='account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.UserAccount'),
        ),
        migrations.AddField(
            model_name='message',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender', to='api.UserAccount'),
        ),
        migrations.AddField(
            model_name='chatroom',
            name='first',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='first_user', to='api.UserAccount'),
        ),
        migrations.AddField(
            model_name='chatroom',
            name='second',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='second_user', to='api.UserAccount'),
        ),
    ]
